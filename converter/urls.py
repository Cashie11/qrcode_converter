from django.urls import path
from converter import views

urlpatterns = [
    path('', views.home, name='home'),
    path('generate/', views.generate_qr, name='generate_qr'),
    path('about/', views.about, name='about'),
]

# Serve media files during development

