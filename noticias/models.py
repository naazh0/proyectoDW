# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from PIL import Image
from django.db import models

# Create your models here.

class Categoria(models.Model):
    name = models.CharField(max_length=144)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Noticia(models.Model):
    name = models.CharField(max_length=144)
    descripcion = models.TextField()
    imagen = models.ImageField(upload_to="projectimg/", null=True, blank=True)
    categoria = models.ForeignKey(Categoria)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_destacada = models.BooleanField()

    def __str__(self):
        return self.name