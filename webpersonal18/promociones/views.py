from django.shortcuts import render
from rest_framework import viewsets
from .serializer import PromoSerializer
from .models import Promocion



# Create your views here.


def promociones(request):
    promociones = Promocion.objects.all()
    return render(request, "promociones/promociones.html", {'promociones':promociones})


class PromoViewset(viewsets.ModelViewSet):
    queryset=Promocion.objects.all()
    serializer_class=PromoSerializer