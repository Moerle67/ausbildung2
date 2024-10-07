from django.db import models

# Create your models here.

class Eigene(models.Model):
    from django.contrib.auth.models import User
    user = models.ForeignKey(User, verbose_name=("Benutzer"), on_delete=models.CASCADE)
    gruppe = models.CharField(("zugeordnete Gruppe"), max_length=50)

    class Meta:
        verbose_name = ("Eigene")
        verbose_name_plural = ("Eigene")
        ordering = ['gruppe',]

    def __str__(self):
        return f"({self.user} - {self.gruppe})"

    def get_absolute_url(self):
        return reverse("Eigene_detail", kwargs={"pk": self.pk})
