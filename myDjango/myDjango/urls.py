from django.contrib import admin
from django.urls import path
from . import views  # Ensure this import statement is correct



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]