from django.shortcuts import render, redirect
from core.models import Evento
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def login_user (request):
    return render(request, 'login.html')

def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        usuario = authenticate(username=username, password=password)
        if usuario   is not None :
            login (request, usuario)
            return redirect('/')
        else:
            messages.error(request, "Usuário ou senha inválido")
    return redirect('/')

def logout_user (request):
    logout(request)
    return redirect("/")

@login_required(login_url='/login/')
def evento(request):
    return render (request, 'evento.html')


@login_required(login_url='/login/')
def lista_eventos (request):
       user = request.user
       evento = Evento.objects.filter(usuario=user)
       #mostra somente os eventos do usuário
       data = {'event': evento}
       return render(request, 'agenda.html', data)
def index(request):
    return redirect('/agenda')


@login_required(login_url='/login/')

def submit_evento(request):

    if request.POST:
        titulo = request.POST.get('titulo')
        data_evento = request.POST.get('datac')
        descricao = request.POST.get('descricao')
        usuario = request.user
        Evento.objects.create(titulo=titulo,
                              descricao = descricao,
                              data_evento= data_evento,
                              usuario=usuario)
    return redirect("/")










