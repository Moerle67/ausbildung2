from django.contrib import admin
from .models import Eigene, Team, Teamzuordnung, Gruppe
# Register your models here.

admin.site.register(Eigene)
admin.site.register(Team)
admin.site.register(Teamzuordnung)
admin.site.register(Gruppe)