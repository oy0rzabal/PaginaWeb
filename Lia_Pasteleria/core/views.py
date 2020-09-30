from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'core/home.html')

def menu(request):
    return render(request, 'core/menu.html')

def equipo(request):
    return render(request, 'core/equipo.html')

def contact(request):
    return render(request, 'core/contact.html')