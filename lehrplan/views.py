from django.shortcuts import render
from django.http import HttpResponse
from .classForm import *

from .models import Rahmenlehrplan, Lernfeld, Block
from django.contrib.auth.models import User

from django.contrib.auth.decorators import permission_required
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


@permission_required('lehrplan_addBlock')
def addBlock(request, nrLernfeld):
    lernfeld = Lernfeld.objects.get(id=nrLernfeld)
    user = request.user
    return HttpResponse(f"{lernfeld} + {user}")