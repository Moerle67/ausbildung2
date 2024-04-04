from django.db import models

# Create your models here.
class Bereich(models.Model):
    name = models.CharField(("Bezeichnung"), max_length=50)
    kommentar = models.TextField(("Kommentart"), blank=True, null=True)
    

    class Meta:
        verbose_name = ("Bereich")
        verbose_name_plural = ("Bereiche")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Bereich_detail", kwargs={"pk": self.pk})



class Aufgabe(models.Model):
    titel = models.CharField(("Aufgabe"), max_length=100)
    bereich = models.ForeignKey(Bereich, verbose_name=("Bereich"), on_delete=models.CASCADE)
    kommentar = models.TextField(("Beschreibung"),blank=True, null=True)
    termin = models.DateTimeField(("Termin"), auto_now=False, auto_now_add=False, blank=True, null=True)
    erstellt = models.DateTimeField(("Erstellt"), auto_now=False, auto_now_add=True)
    bearbeitet = models.DateTimeField(("Bearbeitet"), auto_now=True, auto_now_add=False)
    prio = models.IntegerField(("Priorität"), default=0)
    erledigt = models.BooleanField(("erledigt"), default=False)

    class Meta:
        verbose_name = ("Aufgabe")
        verbose_name_plural = ("Aufgaben")
        ordering = ['-prio','titel']

    def __str__(self):
        return f"{self.titel} {self.prio} ({self.bereich}/{self.erledigt})"

    def get_absolute_url(self):
        return reverse("Aufgabe_detail", kwargs={"pk": self.pk})
