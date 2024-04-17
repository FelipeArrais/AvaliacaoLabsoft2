from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_ingressos, name='view_ingressos'),
    path('compra', views.compra_ingresso, name='compra_ingresso')
]