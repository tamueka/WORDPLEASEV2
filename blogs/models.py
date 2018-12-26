from django.contrib.auth.models import User
from django.db import models


class Blog(models.Model):

    PYTHON = 'PYT'
    DJANGO = 'DJA'
    REST = 'RES'

    CATEGORIAS = (
        (PYTHON, 'Python'),
        (DJANGO, 'Django'),
        (REST, 'Rest')
    )

    PUBLICADO = 'PUB'
    EDITADO = 'EDT'
    ELIMINADO = 'ELM'

    ESTADO = (
        (PUBLICADO, 'Publicado'),
        (EDITADO, 'Editado'),
        (ELIMINADO, 'Eliminado')
    )

    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100)
    texto = models.CharField(max_length=150)
    cuerpo = models.TextField()
    url = models.FileField()
    fecha = models.DateTimeField(auto_now_add=True)
    modificacion = models.DateTimeField(auto_now=True)
    categorias = models.CharField(max_length=3, choices=CATEGORIAS)
    publicado = models.CharField(max_length=3, choices=ESTADO)

    def __str__(self):
        return '{0} ({1})'.format(self.titulo, self.get_categorias_display())