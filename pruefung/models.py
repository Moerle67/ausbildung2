from django.db import models

# Create your models here.

class Beruf(models.Model):
    kurz = models.CharField(("Abkürzung"), max_length=10)
    lang = models.CharField(("Langform"), max_length=250)
    info = models.TextField(("Info"), blank=True, null=True)

    class Meta:
        verbose_name = ("Beruf")
        verbose_name_plural = ("Berufe")

    def __str__(self):
        return f"{self.kurz} / {self.lang}"

    def get_absolute_url(self):
        return reverse("Beruf_detail", kwargs={"pk": self.pk})

class Dokument(models.Model):
    bezeichnung = models.CharField(("Titel"), max_length=50)
    datum = models.DateField(("Datum"), auto_now=False, auto_now_add=False)
    beruf = models.ForeignKey(Beruf, verbose_name=("Beruf"), on_delete=models.SET_NULL, null=True, blank=True)   
    pdf_frage = models.FileField(("Datei Fragen"), upload_to=None, max_length=100, null=True, blank=True)
    pdf_antwort = models.FileField(("Datei Lösungen"), upload_to=None, max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = ("Dokument")
        verbose_name_plural = ("Dokumente")

    def __str__(self):
        return self.bezeichnung

    def get_absolute_url(self):
        return reverse("Dokument_detail", kwargs={"pk": self.pk})

class Schlagwort(models.Model):
    name = models.CharField(("Bezeichnung"), max_length=50)
    beschreibung = models.TextField(("Beschreibung"), null=True, blank=True)
    
    class Meta:
        verbose_name = ("Schlagwort")
        verbose_name_plural = ("Schlagwörter")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Schlagwort_detail", kwargs={"pk": self.pk})

class Frage(models.Model):
    titel = models.CharField(("Titel"), max_length=50)
    nummer = models.CharField(("Nummer"), max_length=50)
    beschreibung = models.TextField(("Beschreibung"), blank=True, null=True)
    frage = models.ImageField(("Frage Bild"), upload_to=None, height_field=None, width_field=None, max_length=None)
    antwort = models.ImageField(("Antwort Bild"), upload_to=None, height_field=None, width_field=None, max_length=None)
    quelle = models.ForeignKey(Dokument, verbose_name=("Quelle"), on_delete=models.SET_NULL, related_name="Frage", null=True, blank=True)
    stichworte = models.ManyToManyField(Schlagwort, verbose_name=("Schlagwörter"))
 
    class Meta:
        verbose_name = ("Frage")
        verbose_name_plural = ("Fragen")

    def __str__(self):
        return f"{self.titel} - {self.quelle.beruf.kurz} ({self.quelle.datum})"

    def get_absolute_url(self):
        return reverse("Frage_detail", kwargs={"pk": self.pk})
