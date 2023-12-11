from django.shortcuts import render 





# Create your views here.
def home(request):
    return render(request, "core/index.html")

def catalogo(request):
    return render(request, "core/catalogo.html")

def contacto(request):
    return render(request, "core/contacto.html")