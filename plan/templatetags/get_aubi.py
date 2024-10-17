from django import template
from ..models import Block, Gruppe, Daytime

register = template.Library()

@register.filter
def get_aubi(temp):
    liste = temp.split(',')
    group= Gruppe.objects.get(name=liste[0])
    year = int(liste[1])
    kw = int(liste[2])
    day = int(liste[3])
    switch_code = liste[5]
    # Tageszeit ganstags abprüfen
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