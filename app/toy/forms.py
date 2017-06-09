from django.forms import ModelForm

from .models import Toy


class ToyForm(ModelForm):
    class Meta:
        model = Toy

