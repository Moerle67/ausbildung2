from django.shortcuts import render, redirect
from django.http import HttpResponse
from .classForm import FormInput, FormTextArea, FormBtnSave, formLinie

from .models import Rahmenlehrplan, Lernfeld, Block, Aubi
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


@permission_required('lehrplan.add_block')
def addBlock(request, nrLernfeld):
    lernfeld = Lernfeld.objects.get(id=nrLernfeld)
    lehrplan = lernfeld.rahmenlehrplan
    aubi = Aubi.objects.get(user=request.user)
    if request.method == 'POST':
        ds = Block()
        ds.aubi = aubi
        ds.lernfeld = lernfeld
        ds.laenge = request.POST["Anzahl UE"]
        ds.beschreibung = request.POST["Inhalt"]
        ds.save()
        return redirect(f"/lehrplan/{lehrplan.id}")
    lst_blocks = Block.objects.filter(aubi=aubi, lernfeld=lernfeld)
    anzahl_ue = FormInput(type="number", label="Anzahl UE")
    inhalt = FormTextArea("Inhalt", rows=6)
    forms = (anzahl_ue, inhalt, formLinie, FormBtnSave )
    content = {
        'lernfeld': lernfeld,
        'lehrplan': lehrplan,
        'lst_blocks': lst_blocks,
        'aubi': aubi,
        'forms': forms,
    }
    return render(request, "block_new.html", content)

@permission_required('lehrplan.delete_block')
def delBlock(request, nrBlock):
    block = Block.objects.get(id=nrBlock)
    lehrplan =block.lernfeld.rahmenlehrplan
    if request.user == block.aubi.user:

        block.delete()
    return redirect(f"/lehrplan/{lehrplan.id}")