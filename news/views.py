from django.shortcuts import render

from django.http import HttpResponse

def newsView(request):
    return HttpResponse('Hola ingEscobedo aca Jose y Luque,Leonardo(virtual) 2025/06/12')
