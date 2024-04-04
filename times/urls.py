from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('todo/', views.todo, name='todo'),
    path('prio_plus/<int:id>', views.prio_plus, name='prio_plus'),
    path('prio_minus/<int:id>', views.prio_minus, name='prio_minus'),
]
