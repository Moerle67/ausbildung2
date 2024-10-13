from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.

class Ausbilder(models.Model):
    user = models.ForeignKey(User, verbose_name=("User"), on_delete=models.RESTRICT)
    color = models.CharField(("Farbe"), max_length=20)
    

    class Meta:
        verbose_name = ("Ausbilder")
        verbose_name_plural = ("Ausbilder")
        beschreibung = models.TextField(("Beschreibung"), null=True, blank=True)
        

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Ausbilderdetail", kwargs={"pk": self.pk})

