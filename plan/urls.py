from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('<int:team>/<int:year>/<int:kw>', views.plan_grob, name = "plan_grob"),
    path('block/<str:var>/<int:aubi_id>/<int:team>', views.block, name='block'),
]