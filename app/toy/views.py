from django.views.generic.edit import UpdateView
from django.views.generic import ListView
from django.urls import reverse_lazy

from .models import Toy


class ToyEditView(UpdateView):
    model = Toy
    fields = '__all__'
    template_name_suffix = '_edit'
    success_url = reverse_lazy('toy:list')


class ToyListView(ListView):

    def get_queryset(self):
        return Toy.objects.all()
