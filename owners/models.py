from django.db import models

# Create your models here.
class Owner(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False, verbose_name="Full Name (*).")
    cpf = models.CharField(max_length=11, null=False, blank=False, verbose_name="CPF (*).")
    telefone = models.CharField(max_length=255, null=False, blank=False, verbose_name="Phone Number (*).")

    def __str__(self):
        return "{} - {}".format(self.name, self.cpf)
