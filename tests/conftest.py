import os
import sys


def pytest_configure():
    project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    sys.path.append(os.path.join(project_root, 'app'))
    os.environ['DJANGO_SETTINGS_MODULE'] = 'settings.test'
    import django
    django.setup()
