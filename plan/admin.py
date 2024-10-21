from django.contrib import admin

from .models import Gruppe, Block, Ausbilder, Daytime, Team, AubiBlock 
# Register your models here.

admin.site.register(Gruppe)
admin.site.register(Ausbilder)
admin.site.register(Daytime)
admin.site.register(AubiBlock)

@admin.register(Block)
class FrageBlock(admin.ModelAdmin):
    list_filter = ['group', 'year', 'kw']

@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    filter_horizontal = ['members', 'groups']
