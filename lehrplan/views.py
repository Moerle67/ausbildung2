from django.shortcuts import render

from .models import Rahmenlehrplan, Lernfeld, Block
# Create your views here.

def start(request, nrlp):
    lst_lehrplan = Rahmenlehrplan.objects.filter(aktiv=True)
    rahmenlehrplan = Rahmenlehrplan.objects.get(id=nrlp)
    lst_lernfelder = Lernfeld.objects.filter(rahmenlehrplan=rahmenlehrplan)
    lst_block = []
    for lernfeld in lst_lernfelder:
        blocks = Block.objects.filter(lernfeld=lernfeld)
        lst_block.append((lernfeld, blocks))
    content = {
        'lst_lehrplan': lst_lehrplan,
        'lst_lernfelder': lst_block,
        'cont': '/lehrplan/1',
    }
    return render(request, "lehrplan.html", content)