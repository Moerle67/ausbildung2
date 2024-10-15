from django.contrib import admin

from .models import Gruppe, Block, Ausbilder, Daytime
# Register your models here.

admin.site.register(Gruppe)
admin.site.register(Ausbilder)
admin.site.register(Daytime)

@admin.register(Block)
class FrageBlock(admin.ModelAdmin):
    list_filter = ['group', 'year', 'kw']
