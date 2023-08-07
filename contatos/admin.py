from django.contrib import admin
from . import models

admin.site.register(models.Grupo)
admin.site.register(models.Contato)
admin.site.register(models.Telefone)
admin.site.register(models.Email)