from django.db import models

# Create your models here.
class Owners(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Nome Completo")
    cpf = models.CharField(max_length=11, null=False, blank=False, verbose_name="CPF")
    telefone = models.CharField(max_length=255, null=False, blank=False, verbose_name="Telefone (*)")

    def __str__(self):
        return "{} - {}".format(self.nome, self.cpf)
