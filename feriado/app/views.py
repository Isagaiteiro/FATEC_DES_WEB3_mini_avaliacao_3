from django.shortcuts import render, redirect
from .models import FeriadoModel

def index(request):
    return render(request, 'index.html')

def route_all_holidays(request):
    List = FeriadoModel.objects.all()
    return render(request, 'all_holidays.html', {'List': List})

#Realizando busca e filtrando a tabela
def route_form(request):
    List = FeriadoModel.objects.all()

    #Django recebe o que foi digitado no input
    busca_nome = request.GET.get('nome')
    busca_dia = request.GET.get('dia')
    busca_mes = request.GET.get('mes')
    #Verifica se foi inserido valor no campo
    if busca_nome:
        #Realiza um filtro na tabela
        List = FeriadoModel.objects.filter(nome_feriado__icontains = busca_nome)
        return render(request, 'form.html', {'List': List})
    
    elif busca_dia:
        List = FeriadoModel.objects.filter(dia__exact = busca_dia)
        return render(request, 'form.html', {'List': List})

    elif busca_mes:
        List = FeriadoModel.objects.filter(mes__exact = busca_mes)
        return render(request, 'form.html', {'List': List})
    else:
        return render(request, 'form.html', {'List': List})
    
