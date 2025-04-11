from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [

    path('<int:team>/<int:year>/<int:kw>', views.plan_grob, name = "plan_grob"),                                                    # Plan anzeigen und bearbeiten
    path('<int:team>', views.plan_prev, name = "plan_prev"),                                                                        # Aufruf mit Abtl.Nr
    path('block/<int:group>/<int:year>/<int:kw>/<int:day>/<str:daytime>/<int:aubi_id>/<int:team>', views.block, name='block'),      # Block speichern
    path('set_content/<int:id>/<str:content>/<int:team>/<int:year>/<int:kw>', views.set_content, name='set_content'),               # Ausb-Inhalt speichern
    path('set_content/<int:id>//<int:team>/<int:year>/<int:kw>', views.clear_content, name='clear_content'),               # Ausb-Inhalt speichern
    path('set_kw/<int:team>/<int:year>/<int:kw>/<int:code>', views.set_kw, name='set_kw'),                                          # KW bestimmen
    path('login', views.user_login, name="login"),                                                                                  # Login
    path('logout', views.user_logout, name="logout"),                                                                               # Logout
    path('block/del/<int:block>/<int:team>', views.block_del, name="block_del"),                                                    # Block löschen
    path('delete_plan/<int:team>/<int:year>/<int:kw>', views.delete_plan, name = "plan_grob"),    
    path('copy_plan/<int:team>/<int:year>/<int:kw>', views.copy_plan, name = "plan_grob"),    
]