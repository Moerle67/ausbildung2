from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Ausbilder(models.Model):
    # user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.RESTRICT, unique=True)
    user = models.OneToOneField(User, verbose_name=("User"), on_delete=models.CASCADE, related_name="User2")
    kuerzel = models.CharField(("Kürzel"), max_length=10)
    color = models.CharField(("Farbe"), max_length=20)
    fg_color = models.CharField(("Schriftfarbe"), max_length=50, default="black")
    beschreibung = models.TextField("Beschreibung", null=True, blank=True)
    activ = models.BooleanField(("Aktiv"), default=True)

    class Meta:
        verbose_name = ("Ausbilder")
        verbose_name_plural = ("Ausbilder")
        ordering = ['user']

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} ({self.user})"
#    def get_absolute_url(self):
#        return reverse("Ausbilderdetail", kwargs={"pk": self.pk})
