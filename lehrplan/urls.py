from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('<int:nrlp>', views.start, name = 'index'),
    path('add_block/<int:nrLernfeld>', views.addBlock, name = 'addBlock'),
]