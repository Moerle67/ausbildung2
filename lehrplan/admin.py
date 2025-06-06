from django.contrib import admin

from .models import Rahmenlehrplan, Beruf, Lernfeld, Aubi, Block

# Register your models here.
admin.site.register(Rahmenlehrplan)
admin.site.register(Beruf)
admin.site.register(Lernfeld)
admin.site.register(Aubi)
admin.site.register(Block)