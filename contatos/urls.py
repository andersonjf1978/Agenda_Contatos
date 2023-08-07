from django.urls import path
from . import views

urlpatterns = [
    path('', views.contatos_list_view, name='contatos_list_view'),
]