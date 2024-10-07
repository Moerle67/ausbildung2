from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Eigene
from .forms import LdokuForm
# Create your views here.

def index(request):
    user = request.user
    if user.is_anonymous:
        form = LdokuForm(request.POST)
        content = {
            "form": form,
            "aim": "/ldoku",
            "gruppen": None,
            "beschwerden":None,
        }
        return render(request, "ldoku.html", content)
    beschwerden = []
    gruppen = Eigene.objects.filter(user=user)
    if request.method == "POST":
        form = LdokuForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data["eingabe"]
            gruppe = form.cleaned_data["gruppe"]
            if len(gruppe)>3 :
                dstest = Eigene.objects.filter(user=user, gruppe=gruppe)
                if len(dstest) == 0:
                    ds = Eigene()
                    ds.gruppe = gruppe
                    ds.user = user
                    ds.save()
                    initial_data = {
                        'eingabe': text,
                        'gruppe': ""
                    }
                    form = LdokuForm(initial=initial_data)
                    gruppen = Eigene.objects.filter(user=user)
        zeilen = text.split('\n')
        for zeile in zeilen:
            for gruppe in gruppen:
                if gruppe.gruppe in zeile:
                    beschwerden.append(zeile)
    else:
        form = LdokuForm(request.POST)
        beschwerden.append("Noch keine")
    
    content = {
        "form": form,
        "aim": "/ldoku",
        "gruppen": gruppen,
        "beschwerden": beschwerden,
    }
    return render(request, "ldoku.html", content)
