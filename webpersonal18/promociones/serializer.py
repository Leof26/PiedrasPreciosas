from rest_framework import serializers
from .models import Promocion

class PromoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Promocion
        #fields= ('title','description')
        fields='__all__'