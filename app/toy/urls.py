from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^(?P<pk>[0-9]+)/$', views.ToyEditView.as_view(), name='edit'),
    url(r'^$', views.ToyListView.as_view(), name='list'),
]
