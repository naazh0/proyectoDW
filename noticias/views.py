# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, get_object_or_404
from noticias.models import Copropietario
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from forms import SignUpForm
from .forms import CopropForm


def detalle_noticia(request, pk):
	template_name = 'noticias/noticia_detalle.html'
	noticia_detalle = Noticia.objects.get(pk=pk)

	return render(request, template_name, {'noticia_detalle':noticia_detalle})

def main(request):
    return render_to_response('noticias/main.html', {}, request)


@login_required()
def home(request):
	object_list = Copropietario.objects.order_by('-created')
	return render_to_response('noticias/index.html', {'user': request.user, 'object_list':object_list}, request)


@login_required()
def perfil(request):
	return render_to_response('noticias/perfil.html', {'user': request.user}, request)

@login_required()
def editar_copro(request):
    form = CopropForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'noticias/editar_copro.html', {'form': form})

    return render_to_response('noticias/editar_copro.html', {'user': request.user, 'form':form}, request)

@login_required()
def copro_delete(request, pk) :
    copropietario = get_object_or_404(Copropietario, pk=pk)
    copropietario.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required()
def copro_update(request, pk) :
    template_name = 'noticias/editar_copro.html'
    # movie = Movie.objects.get(pk=pk)
    copropietario = get_object_or_404(Copropietario, pk=pk)
    # select * from movie WHERE id = xx

    form = CopropForm(request.POST or None, instance=copropietario)

    if form.is_valid() :
        form.save()
        return HttpResponseRedirect(reverse('home'))

    return render(request, template_name, {'form': form})

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


