from django import template
from ..models import Block, Gruppe, Daytime, Team


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
    # Tageszeit ganztags abprüfen
    daytime = Daytime.objects.get(short="gt")
    block = Block.objects.filter(group=group, year=year, kw=kw, day=day, daytime=daytime)
    if len(block)==0:
        daytime = Daytime.objects.get(short=liste[4].strip())
        block = Block.objects.filter(group=group, year=year, kw=kw, day=day, daytime=daytime)
    if len(block) > 0:   
        ds = list(block)[-1]               # mindestens ein Treffer
        if switch_code == "aubi":
            return ds.teacher   # letzter Eintrag
        elif switch_code == "color":
            return ds.teacher.color
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
# Ausbilder suchen, die noch zur Verfügung stehen
    lst_param = value.split(',')
    team_ds = Team.objects.get(name=lst_param[4])
    lst_aubi = team_ds.members.filter(activ=True)
    lst_aubi_ready = []
    daytime_ds = Daytime.objects.get(short=lst_param[3])
    for aubi in lst_aubi:
        # Entsprechende Tageszeit
        ds1 = Block.objects.filter(year=int(lst_param[0]), kw=int(lst_param[1]), day=int(lst_param[2]), daytime=daytime_ds, teacher = aubi)
        # Ganztags
        ds2 = Block.objects.filter(year=int(lst_param[0]), kw=int(lst_param[1]), day=int(lst_param[2]), daytime=Daytime.objects.get(short="gt"), teacher = aubi)
        if len(ds1)==0 and len(ds2)==0:              # Noch kein Einsatz
            lst_aubi_ready.append(aubi)
    
    return lst_aubi_ready