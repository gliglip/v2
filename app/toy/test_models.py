from django.contrib.gis.geos import Point
from django.test import TestCase

from .models import Toy


class ToyModelTest(TestCase):

    # pylint: disable=R0201
    def test_model_create(self):
        # pylint: disable=no-member
        toy, _ = Toy.objects.get_or_create(
            title="test", defaults={"location": Point(1, 1)})
        assert toy.title == "test"
        assert toy.location.srid == 4326
