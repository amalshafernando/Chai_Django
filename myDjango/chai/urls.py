from django.urls import path
from . import views  # Ensure this import statement is correct



urlpatterns = [
    #localhost:8080/chai
    path('', views.all_chai, name='all_chai'),
    path('menu/', views.menu, name='menu'),
    #localhost:8080/chai/order
    #path('order/', views.order, name='order')
    


]