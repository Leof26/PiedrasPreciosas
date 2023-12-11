from django.contrib import admin
from .models import Promocion

# Register your models here.
class PromoAdmin(admin.ModelAdmin):
    readonly_fields=('create','update')



admin.site.register(Promocion, PromoAdmin)

