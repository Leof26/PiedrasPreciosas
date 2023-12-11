from django.urls import path,include
from rest_framework import routers
from promociones import views

router=routers.DefaultRouter()
router.register(r'promocion' ,views.PromoViewset)

urlpatterns = [
    path('', include(router.urls))
]
