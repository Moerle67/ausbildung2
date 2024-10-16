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
    block = Block.objects.filter(group=group, year=year, kw=kw, day=day, daytime=daytime)
    print("ga", len(block))
    # print(block)
    return block