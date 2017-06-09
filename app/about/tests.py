from django.test import TestCase
from django.urls import reverse


class UrlTest(TestCase):

    def test_about_template(self):
        resp = self.client.get(reverse('about:about'))
        assert resp.template_name.pop() == 'about/about.html'

    def test_welcome_template(self):
        resp = self.client.get('/')
        assert resp.template_name.pop() == 'about/welcome.html'
