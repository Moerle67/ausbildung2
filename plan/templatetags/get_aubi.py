from django import template
from ..models import Block, Gruppe, Daytime

register = template.Library()

@register.filter
def get_aubi(group, args):
    print(args)
    numbers = args.split(',')
    #group= Gruppe.objects.get(id=group)
    #daytime = Daytime.objects.get(id=daytime)
    #answer = Block.objects.get(group=group, year=year, kw=kw, day=day, daytime=daytime)
    return numbers