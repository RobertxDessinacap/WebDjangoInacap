from django.db import models

# Create your models here.
class LoginPersonal(models.Model):
    usuario = models.CharField(max_length=100)
    password = models.CharField(max_length=70)

    def __str__(self):
        return self.usuario
