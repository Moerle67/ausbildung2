from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Beruf)
admin.site.register(Dokument)
admin.site.register(Schlagwort)
# admin.site.register(Frage)

@admin.register(Frage)
class FrageAdmin(admin.ModelAdmin):
    filter_horizontal = ['stichworte', ]