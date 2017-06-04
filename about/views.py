from django.views.generic import TemplateView


class WelcomeView(TemplateView):
    template_name = "about/welcome.html"


class AboutView(TemplateView):
    template_name = "about/about.html"
