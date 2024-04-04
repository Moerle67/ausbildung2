from django.shortcuts import redirect, render
from django.urls import reverse
from .models import *  # noqa: F403

# Create your views here.

def index(request):
    return render(request, "times/index.html")

def todo(request):
    aufgaben = Aufgabe.objects.filter(erledigt=False)
    content = {
        'aufgaben': aufgaben
    }
    return render(request, 'times/todo.html', content)

def prio_plus(request, id):
    ds = Aufgabe.objects.get(pk=id)
    ds.prio +=1
    ds.save() 
    return  redirect(reverse('todo'))

def prio_minus(request, id):
    ds = Aufgabe.objects.get(pk=id)
    ds.prio -=1
    ds.save() 
    return  redirect(reverse('todo'))
