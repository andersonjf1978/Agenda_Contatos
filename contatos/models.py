from django.db import models

class Grupo(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    descricao = models.CharField(max_length=280, null=True, blank=True)

class Contato(models.Model):
    nome = models.CharField(max_length=50, unique=True)
    avatar = models.ImageField(upload_to='avatares/', null=True, blank=True)
    grupos = models.ManyToManyField(Grupo)

    class Meta:
        ordering = ['nome']

class Telefone(models.Model):
    numero = models.CharField(max_length=14)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)

class Email(models.Model):
    endereco = models.EmailField(max_length=255)
    contato = models.ForeignKey(Contato, on_delete=models.CASCADE)