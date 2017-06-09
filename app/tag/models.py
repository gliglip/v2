from django.db import models


class Tag(models.Model):
    code = models.CharField(max_length=128, unique=True)
    display_name = models.CharField(max_length=128)

    def __str__(self):
        return self.code

    @staticmethod
    def normalize_name(name):
        name = name.lower()
        # take only alphanumeric, comma and white space from string
        name = ''.join(ch for ch in name if ch.isalnum() or ch == ',' or ch == ' ')
        name = name.replace(',', ' ')
        return '-'.join(name.split())

    # pylint doesn't like the method signature as it is different from
    # how it is defined in django models, but this is the recommended signature
    # https://docs.djangoproject.com/en/1.11/topics/db/models/#overriding-predefined-model-methods
    # pylint: disable-msg=W0221
    def save(self, *args, **kwargs):
        self.code = self.normalize_name(self.display_name)
        return super(Tag, self).save(*args, **kwargs)
