from django.db import models

# Create your models here.

class Project (models.Model):
    title=models.CharField(max_length=200, verbose_name="Titulo")
    description=models.TextField(verbose_name="Descripcion")
    page=models.CharField(max_length=200, verbose_name="Pagina Web" ,null= True, blank=True)
    image=models.ImageField(verbose_name="Imagen", upload_to="projects",null= True, blank=True)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creacion")
    update=models.DateTimeField(auto_now=True, verbose_name="Fecha de actualizacion")
    

    class Meta:
        verbose_name='Proyecto'
        verbose_name_plural='Proyectos'
        ordering=["-created"]

    def __str__(self):
        return self.title