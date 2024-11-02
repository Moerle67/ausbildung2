## todo 
# Liste Plan

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, get_object_or_404, redirect
import datetime

from .models import Gruppe,Team, Block, Ausbilder
# Create your views here.

def user_login(request):
    name = request.POST['name']
    password = request.POST['password']
    cont = request.POST['cont']
    user = authenticate(request, username=name, password=password)
    if user is not None:
        login(request, user)
    return redirect(cont)
    # Redirect to a success page.

def user_logout(request):
    cont = request.POST['cont']
    logout(request)
    return redirect(cont)

def plan_grob(request, team, year, kw):
    team = get_object_or_404(Team, id=team)
    return_aim = f"/plan/{team.id}/{year}/{kw}"
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
                    lst_day.append((ds[0], day))
                else:
                    lst_day.append((("--------", "", "white"), day))
            lst_daytime.append((lst_day, daytime))
        lst_group.append((lst_daytime, gruppe))

    content= {

        "cont": return_aim,
        "liste": lst_group,
        "team": team,
        "year": str(year),
        "kw": str(kw),
        "gruppen": lst_gruppe,
        "daytimes": daytimes,
        "week": week,
        "days": ("0", "1", "2", "3", "4"),
        "weekdays": ("Mo", "Di", "Mi", "Do", "Fr"),
    }
    return render(request, "plan_light.html", content)

def block(request, group, year, kw, day, daytime, aubi_id, team):
    gruppe_ds = Gruppe.objects.get(id=group)
    teacher_ds = Ausbilder.objects.get(id=aubi_id)

    ds, fail = Block.objects.get_or_create(
        group=gruppe_ds, 
        year=year, 
        kw = kw, 
        day = day, 
        daytime = daytime)

    ds.teacher = teacher_ds
    ds.content = ""
    ds.save()

    return redirect(f"/plan/{team}/{year}/{kw}")

def set_content(request, id, content, team, year, kw):
    ds = Block.objects.get(id=id)
    ds.content = content
    ds.save()

    return redirect(f"/plan/{team}/{year}/{kw}")

def set_kw(request, team, year, kw, code):
    if code == 1:
        kw -= 1
        if kw==0:
            year -= 1
            kw = 53
    else:
        kw +=1
        if kw==54:
            year += 1
            kw = 1        
    return redirect(f"/plan/{team}/{year}/{kw}")