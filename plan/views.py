from django.shortcuts import render
import datetime

from .models import Gruppe,Team, Block
# Create your views here.
def plan_grob(request, team, year, kw):
    team = Team.objects.get(id=team)
    d = f"{year}-W{kw}"
    r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
    week = []
    for i in range(5):
        week.append(r.strftime('%d.%m.'))
        r += datetime.timedelta(days=1)
    lst_gruppe = team.groups.filter(activ=True)
    
    daytimes = ("am", "pm")
    content= {
        "team": team,
        "year": str(year),
        "kw": str(kw),
        "gruppen": lst_gruppe,
        "daytimes": daytimes,
        "week": week,
        "days": ("0", "1", "2", "3", "4"),
        "weekdays": ("Mo", "Di", "Mi", "Do", "Fr"),
    }

    return render(request, "plan_grob.html", content)
