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
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.RESTRICT)
    color = models.CharField(("Farbe"), max_length=20)
    beschreibung = models.TextField("Beschreibung", null=True, blank=True)
    

    class Meta:
        verbose_name = ("Ausbilder")
        verbose_name_plural = ("Ausbilder")
        

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user})"
    def get_absolute_url(self):
        return reverse("Ausbilderdetail", kwargs={"pk": self.pk})

class Team(models.Model):

    

    class Meta:
        verbose_name = ("Team")
        verbose_name_plural = ("Teams")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Team_detail", kwargs={"pk": self.pk})
 

class Gruppe(models.Model):
    name = models.CharField(("Bezeichnung"), max_length=50)
    short = models.CharField(("Kürzel"), max_length=10)
    room = models.CharField(("Raum"), max_length=10)
    activ = models.BooleanField(("Aktiv"), default = True)

    class Meta:
        verbose_name = ("Gruppe")
        verbose_name_plural = ("Gruppen")
        ordering = ["-activ", "name"]

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Gruppe_detail", kwargs={"pk": self.pk})
    
class Block(models.Model):
    group = models.ForeignKey(Gruppe, verbose_name=("Gruppe"), on_delete=models.CASCADE)
    year = models.IntegerField(("Jahr"))
    kw = models.IntegerField(("Kalenderwoche"))
    day = models.IntegerField(("Tag"))
    daytime = models.ForeignKey(Daytime, verbose_name=("Tageszeit"), on_delete=models.CASCADE)
    teacher = models.ForeignKey(Ausbilder, verbose_name=("Ausbilder"), on_delete=models.CASCADE)
    content = models.CharField(("Fach"), max_length=50)

    class Meta:
        verbose_name = ("Block")
        verbose_name_plural = ("Blöcke")
        ordering = ["group", "year","kw", "day", "daytime"]

    def __str__(self):
        return f"{self.group.short} - {self.year}/{self.kw}/{self.day}/{self.daytime.short} - {self.teacher.user.last_name}"

    def get_absolute_url(self):
        return reverse("Block_detail", kwargs={"pk": self.pk})



