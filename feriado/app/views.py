from django.shortcuts import render, redirect

from .models import FeriadoModel

def route_all_holidays(request):
    List = FeriadoModel.objects.all()
    
    return render(request, 'all_holidays.html', {'List': List})

#Realizando busca e filtrando a tabela
def route_form(request):
    #Django recebe o que foi digitado no input nome
    busca = request.GET.get('search')
    #Verifica se foi inserido valor no campo
    if busca:
        #Realiza um filtro na tabela
        List = FeriadoModel.objects.filter(nome_feriado__icontains = busca)
    return render(request, 'form.html', {'List': List})
