from django.shortcuts import render, redirect, get_object_or_404

def capa(request):
    return render(request, 'capa.html')
