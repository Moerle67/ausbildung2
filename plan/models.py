import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# 
from stammdaten.models import Ausbilder as Aubi

from lehrplan.models import Block as Lehrblock

# Create your models here.

class Daytime(models.Model):
    short = models.CharField(("Kürzel"), max_length=2)
    description = models.CharField(("Beschreibung"), max_length=50)

    class Meta:
        verbose_name = ("Tageszeit")
        verbose_name_plural = ("Tageszeiten")

    def __str__(self):
        return f"{self.short}/{self.description}"

    def get_absolute_url(self):
        return reverse("Daytime_detail", kwargs={"pk": self.pk})

class Gruppe(models.Model):
    name = models.CharField(("Bezeichnung"), max_length=50, unique=True)
    short = models.CharField(("Kürzel"), max_length=10)
    room = models.CharField(("Raum"), max_length=10)
    activ = models.BooleanField(("Aktiv"), default = True)

    class Meta:
        verbose_name = ("Gruppe")
        verbose_name_plural = ("Gruppen")
        ordering = ["-activ", "name"]

    def __str__(self):
        aktiv = "aktiv" if self.activ else "inactiv"
        return f"{self.name} ({aktiv})"

    def get_absolute_url(self):
        return reverse("Gruppe_detail", kwargs={"pk": self.pk})

class Team(models.Model):
    name = models.CharField(("Bezeichnung"), max_length=50, unique=True)
    comment = models.TextField(("Beschreibung"), null=True, blank=True)
    members = models.ManyToManyField(Aubi, verbose_name=("Ausbilder"), blank=True)
    groups = models.ManyToManyField(Gruppe, verbose_name=("Gruppen"), blank=True)
    activ = models.BooleanField(("Aktiv"), default=True)

    class Meta:
        verbose_name = ("Team")
        verbose_name_plural = ("Teams")
        ordering = ['name']

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})

class Block(models.Model):
    DAYTIME_CHOICES = (
    #    ("gt", "Ganztag"),
        ("am", "Vormittag"),
        ("pm", "Nachmittag"),
    )
    group = models.ForeignKey(Gruppe, verbose_name=("Gruppe"), on_delete=models.CASCADE)
    year = models.IntegerField(("Jahr"))
    kw = models.IntegerField(("Kalenderwoche"))
    day = models.IntegerField(("Tag"))
    daytime = models.CharField(("Tageszeit"), max_length=2, choices=DAYTIME_CHOICES)
    teacher = models.ForeignKey(Aubi, verbose_name=("Ausbilder"), on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(("Info"), max_length=50, null=True, blank=True)
    lehrblock = models.ForeignKey(Lehrblock, verbose_name=("Ausbildungseinheit"), on_delete=models.CASCADE, null=True, blank=True)

    class Meta:
        verbose_name = ("Block")
        verbose_name_plural = ("Blöcke")
        ordering = ["group", "year","kw", "day", "daytime"]

    def __str__(self):
        return f"{self.group.short} - {self.year}/{self.kw}/{self.day}/{self.get_daytime_display()} - {'' if self.teacher is None else self.teacher.user.last_name}"

    def get_absolute_url(self):
        return reverse("Block_detail", kwargs={"pk": self.pk})


class AubiBlock(models.Model):
    WD_CHOICES = (
        (0, 'Montag'),
        (1, 'Dienstag'),
        (2, 'Mittwoch'),
        (3, 'Donnerstag'),
        (4, 'Freitag')
    )
    DAYTIME_CHOICES = (
        ("gt", "Ganztag"),
        ("am", "Vormittag"),
        ("pm", "Nachmittag"),
    )
    aubi = models.ForeignKey(Aubi, verbose_name=("Ausbilder"), on_delete=models.CASCADE)
    date = models.DateField(("Datum"), auto_now=False, auto_now_add=False, null=True, blank=True)
    day = models.IntegerField(("Wochentag)"), choices=WD_CHOICES, null=True, blank=True)
    daytime = models.CharField(("Tageszeit"), max_length=2, choices=DAYTIME_CHOICES, default="gt")
    comment = models.TextField(("Kommentar"), null=True, blank=True)
    class Meta:
        verbose_name = ("AubiBlock")
        verbose_name_plural = ("AubiBlocks")

    def __str__(self):
        return f"{self.aubi} ({'' if self.date is None else self.date}{'' if self.day is None else self.day} - {self.daytime})"

    def get_absolute_url(self):
        return reverse("AubiBlock_detail", kwargs={"pk": self.pk})

class Log(models.Model):
    user = models.ForeignKey(User, verbose_name=("Benutzer"), on_delete=models.CASCADE)
    block = models.ForeignKey(Block, verbose_name=("Ausbildungsblock"), on_delete=models.CASCADE)
    time = models.DateTimeField(("Zeitpunkt"), auto_now=False, auto_now_add=True)
    description = models.CharField(("Tätigkeit"), max_length=50)

    class Meta:
        verbose_name = "Log"
        verbose_name_plural = "Logs"

    def __str__(self):
        return f"{self.block} - {self.user}/{self.time}"

    def get_absolute_url(self):
        return reverse("Log_detail", kwargs={"pk": self.pk})
    
class JourFixe(models.Model):
    gruppe = models.ForeignKey(Gruppe, verbose_name="Gruppe", on_delete=models.CASCADE)
    datum = models.DateTimeField(("Zeitpunkt"), auto_now=False, auto_now_add=False)
    aktiv = models.BooleanField(("Aktiv"), default=True)

    class Meta:
        verbose_name = "JourFixe"
        verbose_name_plural = "JourFixes"

    def __str__(self):
        return f"{self.gruppe}-{self.datum} ({self.get_daytime})"

    def get_absolute_url(self):
        return reverse("JourFixe_detail", kwargs={"pk": self.pk})

    @property
    def get_daytime(self):
        print(self.datum.time,datetime.time(12, 00))
        if self.datum.time() < datetime.time(12, 00):
            return "am"
        else:
            return "pm"
        