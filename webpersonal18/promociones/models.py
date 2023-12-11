from django.db import models

# Create your models here.
class Promocion(models.Model):
    title=models.CharField(max_length=50, verbose_name = 'titulo')
    description=models.TextField(verbose_name = 'descripcion')
    image=models.ImageField(verbose_name = 'imagen' , upload_to="projects")
    create=models.DateTimeField(auto_now_add=True, verbose_name = 'fecha de creacion')
    update=models.DateTimeField(auto_now=True, verbose_name = 'fecha de modificacion')
    
    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'promocion'
        verbose_name_plural = 'promociones'
        ordering = ['-create']