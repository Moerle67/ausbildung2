from django import forms
from django.contrib.auth.models import User

class LdokuForm(forms.Form):
    eingabe = forms.CharField(label="Eingabe",widget=forms.Textarea(attrs={"rows":"15"}), required=False)
    gruppe = forms.CharField(max_length=50, required=False)