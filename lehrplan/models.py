from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

from stammdaten.models import Ausbilder as Aubi


# Create your models here.

class Rahmenlehrplan(models.Model):
    date = models.DateField("Version")
    bereich = models.CharField("Bereich", max_length=50)
    description = models.TextField(("Beschreibung"), blank=True, null=True)
    bundesland = models.CharField(("Beschreibung"), max_length=50, default="Baden-Württemberg")
    quelle = models.URLField("Quelle", max_length=200)
    aktiv = models.BooleanField(("aktiv"), default=True)
    class Meta:
        verbose_name = ("Rahmenlehrplan")
        verbose_name_plural = ("Rahmenlehrpläne")

    def __str__(self):
        return f"{self.bereich} - {self.bundesland} vom {self.date}"

    def get_absolute_url(self):
        return reverse("Daytime_detail", kwargs={"pk": self.pk})

class Beruf(models.Model):
    kuerzel = models.CharField(("Kürzel"), max_length=5)
    name = models.CharField(("Name"), max_length=50)
    beschreibung = models.TextField(("Beschreibung"), null=True, blank=True)
    
    class Meta:
        verbose_name = ("Beruf")
        verbose_name_plural = ("Berufe")

    def __str__(self):
        return f"{self.kuerzel} - {self.name}"

    def get_absolute_url(self):
        return reverse("Beruf_detail", kwargs={"pk": self.pk})

class Lernfeld(models.Model):
    rahmenlehrplan = models.ForeignKey(Rahmenlehrplan, verbose_name=("Rahmenlehrplan"), on_delete=models.RESTRICT)
    nummer = models.CharField(("Nummer"), max_length=5)
    inhalt = models.CharField(("Inhalt"), max_length=200)
    stunden1 = models.IntegerField(("Zeitrichtwerte 1. Jahr"), default = 0)
    stunden2 = models.IntegerField(("Zeitrichtwerte 2. Jahr"), default = 0)
    stunden3 = models.IntegerField(("Zeitrichtwerte 3. Jahr"), default = 0)
    berufe = models.ManyToManyField(Beruf, verbose_name=("Berufe"))
    beschreibung = models.TextField(("Beschreibung"))


    @property
    def get_stunden(self):
        return self.stunden1 + self.stunden2 + self.stunden3
    
    @property
    def get_block_stunden(self):
        lst_block = Block.objects.filter(lernfeld=self)
        stunden = 0
        for block in lst_block:
            stunden += block.laenge
        return stunden

    @property
    def get_berufe(self):
        berufe = ""
        lst_berufe = self.berufe.all()
        for beruf in lst_berufe:
            berufe += beruf.kuerzel + " / "
        return berufe[:-2]   
         
    class Meta:
        verbose_name = ("Lernfeld")
        verbose_name_plural = ("Lernfelder")
        ordering = ["rahmenlehrplan", "nummer"]
        
    def __str__(self):
        return f"{self.nummer} {self.inhalt} {self.get_berufe} ({self.get_block_stunden}/{self.get_stunden} Stunden)"

    def get_absolute_url(self):
        return reverse("Lernfeld_detail", kwargs={"pk": self.pk})


# class Aubi(models.Model):
#     name = models.CharField(("Name"), max_length=150)
#     kuerzel = models.CharField(("Kürzel"), max_length=5)
#     user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE, blank=True, null=True)
#     aktiv = models.BooleanField(("aktiv"), default=True)

#     class Meta:
#         verbose_name = ("Ausbilder")
#         verbose_name_plural = ("Ausbilder")

#     def __str__(self):
#         return f"{self.kuerzel} - {self.name}"

#     def get_absolute_url(self):
#         return reverse("Aubi_detail", kwargs={"pk": self.pk})
    

class Block(models.Model):
    aubi = models.ForeignKey(Aubi, verbose_name=("Ausbilder"), on_delete=models.CASCADE, related_name="AubiRLP")
    lernfeld = models.ForeignKey(Lernfeld, verbose_name=("Lernfeld"), on_delete=models.CASCADE)
    laenge = models.IntegerField(("cia Ausbildungseinheiten"))
    inhalt = models.CharField(("Inhalt"), max_length=30)
    beschreibung = models.TextField(("Beschreibung"))

    class Meta:
        verbose_name = ("Block")
        verbose_name_plural = ("Blöcke")
        ordering = ["aubi", "lernfeld"]

    def __str__(self):
        return f"{self.aubi}-{self.lernfeld.nummer}/{self.inhalt} ({self.laenge} Stunden)"

    def get_absolute_url(self):
        return reverse("_detail", kwargs={"pk": self.pk})

