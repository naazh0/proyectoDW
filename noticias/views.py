# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from noticias.models import Noticia



def index(request):

	object_list = Noticia.objects.order_by('-created')[:7]
	noticia_destacada = Noticia.objects.filter(is_destacada=True).order_by('-created')[:1]

	template = 'noticias/index.html'
	
	return render(request, template, {'object_list':object_list, 'noticia_destacada':noticia_destacada})


def detalle_noticia(request, pk):
	template_name = 'noticias/noticia_detalle.html'
	noticia_detalle = Noticia.objects.get(pk=pk)

	return render(request, template_name, {'noticia_detalle':noticia_detalle})

