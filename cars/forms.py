from django.core.exceptions import ValidationError
from django import forms
from .models import Car


class CarForm(forms.ModelForm):

    class Meta:
        model = Car
        fields = '__all__'

    def clean_owner(self):
        owner = self.cleaned_data['owner']
        cars_count = Car.objects.filter(owner_id=owner.pk)
        if cars_count.count() >= 3:
            raise ValidationError("Error: Person may have up to 3 vehicles")
        else:
            return owner