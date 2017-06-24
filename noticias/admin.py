# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Categoria, Noticia

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id','name','created','modified')
    #list_filter = ('owner','active')
    search_fields = ('id',)

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('id','name','descripcion','categoria','created','modified', 'is_destacada')
    #list_filter = ('owner','active')
    search_fields = ('id',)

admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Noticia, NoticiaAdmin)