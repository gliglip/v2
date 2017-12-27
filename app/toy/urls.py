from django.urls import path

from . import views

app_name = 'toy'
urlpatterns = [
    path('<int:pk>/', views.ToyEditView.as_view(), name='edit'),
    path('', views.ToyListView.as_view(), name='list'),
]
