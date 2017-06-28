# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from noticias.models import Copropietario
from django.template.context import RequestContext
from django.http.response import HttpResponseRedirect
from django.contrib.auth.models import User, Group
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
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
    copropietario = User.objects.all()
    return render_to_response('noticias/index.html', {'copropietario': copropietario, 'user':request.user}, request)


@login_required()
def perfil(request):
	return render_to_response('noticias/perfil.html', {'user': request.user}, request)



@login_required()
def copro_delete(request, pk) :
    copropietario = get_object_or_404(User, pk=pk)
    copropietario.delete()
    return HttpResponseRedirect(reverse('home'))

@login_required()
def copro_update(request, pk) :
    template_name = 'noticias/editar_copro.html'
    # movie = Movie.objects.get(pk=pk)
    user = get_object_or_404(User, pk=pk)
    # select * from movie WHERE id = xx

    form = CopropForm(request.POST or None, instance=user)

    if form.is_valid() :
        form.save()
        return HttpResponseRedirect(reverse('home'))

    return render(request, template_name, {'form': form})

@login_required()
def editar_copro(request):
    form = CopropForm(request.POST or None)
    if form.is_valid() :
        form.save()
        return HttpResponseRedirect(reverse('home'))

    return render(request, 'noticias/editar_copro.html', {'form': form})

    return render_to_response('noticias/editar_copro.html', {'user': request.user, 'form':form}, request)

def signup_copropietario(request):
    

    form = SignUpForm(request.POST or None)

    if form.is_valid() :
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = User.objects.get(username=username)
        
        
        user.set_password(raw_password)
        user.is_staff = False
        user.save()
        return redirect('main')

    else:
        form = SignUpForm()
    return render(request, 'noticias/signup_copropietario.html', {'form': form})
    
@login_required()
def signup_administrador(request):
    

    form = SignUpForm(request.POST or None)

    if form.is_valid() :
        form.save()
        username = form.cleaned_data.get('username')
        raw_password = form.cleaned_data.get('password')
        user = User.objects.get(username=username)
        user.set_password(raw_password)
        user.is_staff = True
        user.save()
        return redirect('main')

    else:
        form = SignUpForm()
    return render(request, 'noticias/signup_administrador.html', {'form': form})

    



