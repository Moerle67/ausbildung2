## todo 
# Liste Plan

from django.shortcuts import render, get_object_or_404, redirect
import datetime

from .models import Gruppe,Team, Block, Ausbilder
# Create your views here.
def plan_grob(request, team, year, kw):
    team = get_object_or_404(Team, id=team)
    lst_ds_group = team.groups.filter(activ=True)
    d = f"{year}-W{kw}"
    r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
    week = []
    for i in range(5):
        week.append(r.strftime('%d.%m.'))
        r += datetime.timedelta(days=1)
    lst_gruppe = team.groups.filter(activ=True)
    daytimes = ("am", "pm")

    # Liste füllen
    lst_group=[]
    for gruppe in lst_ds_group:
        lst_daytime=[]
        for daytime in daytimes:
            lst_day = []
            for day in range(5):
                ds = Block.objects.filter(group=gruppe, year=year, kw=kw, day=day, daytime=daytime)
                if len(ds) != 0:   # Datensatz vorhanden
                    lst_day.append(((ds[0].teacher, ds[0].content, ds[0].teacher.color ), day))
                else:
                    lst_day.append((("--------", "", "white"), day))
            lst_daytime.append((lst_day, daytime))
        lst_group.append((lst_daytime, daytime))

    print(lst_group)
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

def block(request, var, aubi_id, team):
    var_lst = (var).split(',')
    gruppe_ds = Gruppe.objects.get(name=var_lst[0])
    teacher_ds = Ausbilder.objects.get(id=aubi_id)

    ds, fail = Block.objects.get_or_create(
        group=gruppe_ds, 
        year=int(var_lst[1]), 
        kw = int(var_lst[2]), 
        day = int(var_lst[3]), 
        daytime = var_lst[4])

    ds.teacher = teacher_ds
    ds.save()

    return redirect(f"/plan/{team}/{var_lst[1]}/{var_lst[2]}")
