import os


def pytest_configure():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.test'
    import django
    django.setup()
