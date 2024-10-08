from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Eigene(models.Model):
    user = models.ForeignKey(User, verbose_name=("Benutzer"), on_delete=models.CASCADE)
    gruppe = models.CharField(("zugeordnete Gruppe"), max_length=50)

    class Meta:
        verbose_name = ("Eigene")
        verbose_name_plural = ("Eigene")
        ordering = ['gruppe',]

    def __str__(self):
        return f"({self.user} - {self.gruppe})"

    #def get_absolute_url(self):
    #    return reverse("Eigene_detail", kwargs={"pk": self.pk})

class Team(models.Model):
    name = models.CharField(("Bezeichnung"), max_length=10)
    leader = models.ForeignKey(User, verbose_name=("Leiter"), on_delete=models.PROTECT)
    standort = models.CharField(("Standort"), max_length=50)
    beschreibung = models.TextField(("Informationen"),blank=True, null=True)

    class Meta:
        verbose_name = ("Team")
        verbose_name_plural = ("Teams")

    def __str__(self):
        return f"{self.name} ({self.standort}/{self.leader.first_name} {self.leader.last_name})"

    #def get_absolute_url(self):
    #    return reverse("Team_detail", kwargs={"pk": self.pk})

class Gruppe(models.Model):
    name = models.CharField(("Name"), max_length=10)
    team = models.ForeignKey(Team, verbose_name=("Team"), on_delete=models.RESTRICT)

    class Meta:
        verbose_name = ("Gruppe")
        verbose_name_plural = ("Gruppen")

    def __str__(self):
        return f"'{self.name}' -- {self.team}"

    #def get_absolute_url(self):
    #    return reverse("Gruppe_detail", kwargs={"pk": self.pk})

class Teamzuordnung(models.Model):
    user = models.ForeignKey(User, verbose_name=("Ausbilder"), on_delete=models.CASCADE)
    team = models.ForeignKey(Team, verbose_name=("Gruppe"), on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = ("Teamzuordnung")
        verbose_name_plural = ("Teamzuordnungen")
        ordering = ['user',]

    def __str__(self):
        return f"{self.user} - {self.team}"

    #def get_absolute_url(self):
    #    return reverse("Teamzuordnung_detail", kwargs={"pk": self.pk})

