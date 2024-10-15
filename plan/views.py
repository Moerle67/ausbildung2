from django.shortcuts import render
import datetime

from .models import Gruppe
# Create your views here.
def plan_grob(request, year, kw):
    d = f"{year}-W{kw}"
    r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
    week = []
    for i in range(5):
        week.append(r.strftime('%d.%m.'))
        r += datetime.timedelta(days=1)
    lst_gruppe = Gruppe.objects.filter(activ=True)
    daytimes = ("am", "pm")
    content= {
        "year": year,
        "kw": kw,
        "gruppen": lst_gruppe,
        "daytimes": daytimes,
        "week": week,
        "range1": range(5),
        "weekdays": ("Mo", "Di", "Mi", "Do", "Fr"),
    }

    return render(request, "plan_grob.html", content)
