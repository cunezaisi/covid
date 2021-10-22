"""mysite URL Configuration

[...]
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('registro/', views.registrar_usuario, name='registrar_usuario'),
    path('seguimiento/',views.enfermedad_view, name='enfermedad_form'),
    path('generadorQr/',views.generadorQr_view, name='generadorQr'),
    path('consulta/', views.enfermedad_list, name='enfermedad_list'),
]