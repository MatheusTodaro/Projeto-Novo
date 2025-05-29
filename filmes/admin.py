from django.contrib import admin
from .models import Filme
from .models import Genero, Diretor

class FilmeAdmin(admin.ModelAdmin):
        list_display = ('titulo','genero','duracao','ano','diretor')
        search_fields = ('titulo','genero','diretor')

admin.site.register(Filme,FilmeAdmin)

class GeneroAdmin(admin.ModelAdmin):
        list_display= ('nome',)
        search_fields = ('nome',)

admin.site.register(Genero,GeneroAdmin)

class DiretorAdmin(admin.ModelAdmin):
        list_display = ('nome',)
        search_fields =('nome',)

admin.site.register(Diretor,DiretorAdmin)