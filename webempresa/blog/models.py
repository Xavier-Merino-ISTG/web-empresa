from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100, verbose_name="Nombre")
    creado = models.DateField(auto_now_add=True, verbose_name="Fecha de creacion")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "categoria"
        verbose_name_plural = "categorias"
        ordering = ['-creado']

    def __str__(self):
        return self.nombre

class Entrada(models.Model):
    titulo = models.CharField(max_length=200, verbose_name="Titulo")
    contenido = models.TextField(verbose_name="Contenido")
    publicacion = models.DateTimeField(verbose_name="Fecha publicacion", default=timezone.now())
    imagen = models.ImageField(verbose_name="Imagen", upload_to="blog", null=True, blank=True)
    # Clave foranea
    autor = models.ForeignKey(User, verbose_name="Autor", on_delete=models.CASCADE)
    # Relacion muchos a muchos
    categorias = models.ManyToManyField(Categoria, verbose_name="Categorias")
    creado = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creacion")
    actualizado = models.DateTimeField(auto_now=True, verbose_name="Fecha de edicion")

    class Meta:
        verbose_name = "entrada"
        verbose_name_plural = "entradas"
        ordering = ['-creado']

    def __str__(self):
        return self.titulo