from django.db import models

# Create your models here.

class Rahmenlehrplan(models.Model):
    date = models.DateField("Version")
    bereich = models.CharField("Bereich", max_length=50)
    description = models.TextField(("Beschreibung"), blank=True, null=True)
    bundesland = models.CharField(("Beschreibung"), max_length=50, default="Baden-Württemberg")
    quelle = models.URLField("Quelle", max_length=200)

    class Meta:
        verbose_name = ("Rahmenlehrplan")
        verbose_name_plural = ("Rahmenlehrpläne")

    def __str__(self):
        return f"{self.bereich} - {self.bundesland} vom {self.date}"

    def get_absolute_url(self):
        return reverse("Daytime_detail", kwargs={"pk": self.pk})

