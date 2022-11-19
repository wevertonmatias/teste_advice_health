from django.db import models

# Create your models here.
class ColorCar(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)

    def __str__(self):
        return self.description


class ModelsCar(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    
    def __str__(self):
        return self.description


class Car(models.Model):
    description = models.CharField(max_length=255, null=False, blank=False)
    color = models.ForeignKey(ColorCar, on_delete=models.SET_NULL, null=True, blank=False)
    model_car = models.ForeignKey(ModelsCar, on_delete=models.SET_NULL, null=True, blank=False)