# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import AdminCondominio, Copropietario

# Register your models here.



class AdminCondoAdmin(admin.ModelAdmin):
    list_display = ('id','name','rut','correo','fono','created','modified')
    #list_filter = ('owner','active')
    search_fields = ('id',)

class CopropietarioAdmin(admin.ModelAdmin):
    list_display = ('id','name','rut','correo','fono','created','modified')
    #list_filter = ('owner','active')
    search_fields = ('id',)


admin.site.register(AdminCondominio, AdminCondoAdmin)
admin.site.register(Copropietario, CopropietarioAdmin)
