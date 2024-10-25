from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('<int:team>/<int:year>/<int:kw>', views.plan_grob, name = "plan_grob"),
    path('block/<int:group>/<int:year>/<int:kw>/<int:day>/<str:daytime>/<int:aubi_id>/<int:team>', views.block, name='block'),
    path('set_content/<int:id>/<str:content>/<int:team>/<int:year>/<int:kw>', views.set_content, name='set_content'),
]