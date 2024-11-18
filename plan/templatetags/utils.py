from django import template
from ..models import Block, Gruppe, Team, AubiBlock
import datetime
from django.db.models import Q
register = template.Library()

@register.filter
def get_at_index(list, index):
    return list[int(index)]

@register.filter
def get_aubi(temp):
    liste = temp.split(',')
    group= Gruppe.objects.get(name=liste[0])
    year = int(liste[1])
    kw = int(liste[2])
    day = int(liste[3])
    switch_code = liste[5]

    # Entsprechende Tageszeit prüfen
    daytime = liste[4]
    block = Block.objects.filter(group=group, year=year, kw=kw, day=day, daytime=daytime)
    if len(block) > 0:   
        ds = list(block)[-1]               # mindestens ein Treffer
        if switch_code == "aubi":
            return ds.teacher   # letzter Eintrag
        elif switch_code == "color":
            return "white" if ds.teacher is None else ds.teacher.color
        elif switch_code == "fach":
            return ds.content
    else:
        return "--------"
    return "error"

@register.filter
def to_str(value):
    return str(value)

@register.filter
def get_ready_aubi(value):
    IDX_YEAR = 0
    IDX_KW = 1
    IDX_DAY = 2
    IDX_DAYTIME = 3
    IDX_TEAM = 4

# Ausbilder suchen, die noch zur Verfügung stehen
    lst_param = value.split(',')
    team_ds = Team.objects.get(name=lst_param[IDX_TEAM])
    lst_aubi = team_ds.members.filter(activ=True)
    lst_aubi_ready = []
    daytime = lst_param[IDX_DAYTIME]
    for aubi in lst_aubi:
        ## Prüfung allgemeine Abwesenheit
        # Wochentag
        ds = AubiBlock.objects.filter(Q(daytime="gt") | Q(daytime=daytime), aubi=aubi, day=lst_param[IDX_DAY])
        if len(ds)>0:    
            continue    
        # Datum ermitteln
        d = f"{int(lst_param[IDX_YEAR])}-W{int(lst_param[IDX_KW])}"
        r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
        r += datetime.timedelta(days=int(lst_param[IDX_DAY]))
        # Ganztags
        ds = AubiBlock.objects.filter(aubi=aubi, date=r, daytime="gt")
        if len(ds)>0:  
            continue    
        # Tageszeit
        ds = AubiBlock.objects.filter(aubi=aubi, date=r, daytime=daytime)
        if len(ds)>0:       
            continue 

        # Aktuellen Ausbildungsplan prüfen    
        # Entsprechende Tageszeit
        ds1 = Block.objects.filter(year=int(lst_param[IDX_YEAR]), kw=int(lst_param[IDX_KW]), day=int(lst_param[IDX_DAY]), daytime=daytime, teacher = aubi)
        if len(ds1)==0:              # Noch kein Einsatz
            lst_aubi_ready.append(aubi)
    
    return lst_aubi_ready

@register.filter
def get_block_aubi(value):
    IDX_YEAR = 0
    IDX_KW = 1
    IDX_DAY = 2
    IDX_TEAM = 3

    lst_param = value.split(',')
    d = f"{int(lst_param[IDX_YEAR])}-W{int(lst_param[IDX_KW])}"
    r = datetime.datetime.strptime(d + '-1', "%Y-W%W-%w")
    r += datetime.timedelta(days=int(lst_param[IDX_DAY]))
    team_ds = Team.objects.get(name=lst_param[IDX_TEAM])
    lst_aubi = team_ds.members.filter(activ=True)
    lst_aubi_block = []

    for aubi in lst_aubi:
        # Ganztags
        ds0 = AubiBlock.objects.filter(aubi=aubi, day=lst_param[IDX_DAY], daytime="gt")
    
        # Entsprechenden Wochentag
        ds1 = AubiBlock.objects.filter(aubi=aubi, day=lst_param[IDX_DAY])

        # Entsprechendes Datum
        ds2 = AubiBlock.objects.filter(aubi=aubi, date=r)
        if len(ds0) > 0:
            ds = list(ds1)[-1]
            lst_aubi_block.append((aubi,"gt",ds.comment))
        elif len(ds1) > 0:
            ds = list(ds1)[-1]
            lst_aubi_block.append((aubi,ds.daytime,ds.comment))
        elif len(ds2) > 0:
                ds = list(ds2)[-1]
                lst_aubi_block.append((aubi,ds.daytime,ds.comment))

    return lst_aubi_block