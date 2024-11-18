from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

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

class Ausbilder(models.Model):
    # user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.RESTRICT, unique=True)
    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE)
    color = models.CharField(("Farbe"), max_length=20)
    beschreibung = models.TextField("Beschreibung", null=True, blank=True)
    activ = models.BooleanField(("Aktiv"), default=True)

    class Meta:
        verbose_name = ("Ausbilder")
        verbose_name_plural = ("Ausbilder")
        ordering = ['user']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user})"
    def get_absolute_url(self):
        return reverse("Ausbilderdetail", kwargs={"pk": self.pk})

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
    members = models.ManyToManyField(Ausbilder, verbose_name=("Ausbilder"), null=True, blank=True)
    groups = models.ManyToManyField(Gruppe, verbose_name=("Gruppen"), null=True, blank=True)
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
#        ("gr", "Ganztags"),
        ("am", "Vormittag"),
        ("pm", "Nachmittag"),
    )
    group = models.ForeignKey(Gruppe, verbose_name=("Gruppe"), on_delete=models.CASCADE)
    year = models.IntegerField(("Jahr"))
    kw = models.IntegerField(("Kalenderwoche"))
    day = models.IntegerField(("Tag"))
    daytime = models.CharField(("Tageszeit"), max_length=2, choices=DAYTIME_CHOICES)
    teacher = models.ForeignKey(Ausbilder, verbose_name=("Ausbilder"), on_delete=models.CASCADE, null=True, blank=True)
    content = models.CharField(("Fach"), max_length=50, null=True, blank=True)

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
#        ("gr", "Ganztags"),
        ("am", "Vormittag"),
        ("pm", "Nachmittag"),
    )
    aubi = models.ForeignKey(Ausbilder, verbose_name=("Ausbilder"), on_delete=models.CASCADE)
    date = models.DateField(("Datum"), auto_now=False, auto_now_add=False, null=True, blank=True)
    day = models.IntegerField(("Wochentag)"), choices=WD_CHOICES, null=True, blank=True)
    daytime = models.CharField(("Tageszeit"), max_length=2, choices=DAYTIME_CHOICES)
    comment = models.TextField(("Kommentar"), null=True, blank=True)
    class Meta:
        verbose_name = ("AubiBlock")
        verbose_name_plural = ("AubiBlocks")

    def __str__(self):
        return f"{self.aubi} ({'' if self.date is None else self.date}{'' if self.day is None else self.day} - {self.daytime})"

    def get_absolute_url(self):
        return reverse("AubiBlock_detail", kwargs={"pk": self.pk})

