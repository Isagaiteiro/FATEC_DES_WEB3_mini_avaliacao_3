from django.shortcuts import render, redirect

from .models import FeriadoModel

def route_all_holidays(request):
    List = FeriadoModel.objects.all()
    
    return render(request, 'all_holidays.html', {'List': List})
