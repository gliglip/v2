from django.contrib.gis.geos import Point
from django.test import TestCase
from django.urls import reverse

from .models import Toy


class ToyViewTest(TestCase):

    def test_list_view(self):
        resp = self.client.get(reverse('toy:list'))
        assert resp.template_name.pop() == 'toy/toy_list.html'
        assert resp.status_code == 200

    def test_edit_view(self):
        toy, _ = Toy.objects.get_or_create(
            title="test", defaults={"location": Point(1, 1)})

        resp = self.client.get(reverse('toy:edit', args=[toy.id]))
        assert resp.template_name.pop() == 'toy/toy_edit.html'
        assert resp.status_code == 200
