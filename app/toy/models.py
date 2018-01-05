from django.contrib.gis.db.models import GeometryField
from django.db import models
from django.utils.translation import gettext_lazy as _


class Toy(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    location = GeometryField(srid=4326, help_text=_('Used to find nearby users'))

    def __str__(self):
        return self.title
