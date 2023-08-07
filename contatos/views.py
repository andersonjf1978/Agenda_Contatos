from django.shortcuts import render
from .models import Contato

def contatos_list_view(request):
    contatos = Contato.objects.all()
    return render(request, 'contatos/contatos_list.html', {'contatos':contatos})