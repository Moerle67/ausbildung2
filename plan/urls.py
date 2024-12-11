from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

    path('<int:team>/<int:year>/<int:kw>', views.plan_grob, name = "plan_grob"),
    path('<int:team>', views.plan_prev, name = "plan_prev"),
    path('block/<int:group>/<int:year>/<int:kw>/<int:day>/<str:daytime>/<int:aubi_id>/<int:team>', views.block, name='block'),
    path('set_content/<int:id>/<str:content>/<int:team>/<int:year>/<int:kw>', views.set_content, name='set_content'),
    path('set_kw/<int:team>/<int:year>/<int:kw>/<int:code>', views.set_kw, name='set_kw'),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
    # Block löschen
    path('block/del/<int:block>/<int:team>', views.block_del, name="block_del"),
]