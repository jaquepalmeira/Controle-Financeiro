from django.db import models


class Pessoa(models.Model):
    class Meta:
        abstract = True

    nome = models.CharField(max_length=100)
    data_nascimento = models.DateField()
    email = models.EmailField()