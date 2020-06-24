from django.shortcuts import render, redirect
from core.models import Evento




# Create your views here.
def index(request):
    return redirect('/agenda')

def lista_eventos (request):
    usuario = request.user
    evento = Evento.objects.all()
    #mostra somente os eventos do usuário
    data = {'event': evento}
    return render(request, 'agenda.html', data)







