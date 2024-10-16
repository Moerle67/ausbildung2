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
    daytime = Daytime.objects.get(short=liste[4].strip())
    switch_code = liste[5]
    block = Block.objects.filter(group=group, year=year, kw=kw, day=day, daytime=daytime)
    if len(block) > 0:                  # mindestens ein Treffer
        if switch_code == "aubi":
            ds = list(block)[-1]
            return ds.teacher   # letzter Eintrag
    else:
        return "--------"
    return "error"