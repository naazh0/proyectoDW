# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response
from noticias.models import Noticia
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from forms import SignUpForm






def detalle_noticia(request, pk):
	template_name = 'noticias/noticia_detalle.html'
	noticia_detalle = Noticia.objects.get(pk=pk)

	return render(request, template_name, {'noticia_detalle':noticia_detalle})

def main(request):
    return render_to_response('noticias/main.html', {}, request)


@login_required()
def home(request):
	object_list = Noticia.objects.order_by('-created')[:7]
	noticia_destacada = Noticia.objects.filter(is_destacada=True).order_by('-created')[:1]
	return render_to_response('noticias/index.html', {'user': request.user, 'object_list':object_list, 'noticia_destacada':noticia_destacada}, request)


@login_required()
def perfil(request):
	return render_to_response('noticias/perfil.html', {'user': request.user}, request)


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():  
 
            
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
 
            
            
            
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
 
            
            user.save()
 
            return HttpResponseRedirect(reverse('index'))
    else:
        form = SignUpForm()
 
    data = {
        'form': form,
    }
    return render_to_response('noticias/signup.html', data, request)

