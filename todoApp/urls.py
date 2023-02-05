from django.urls import path 
from . import views

urlpatterns = [
    path('',views.Home, name='index'),
    path('udpate/<str:pk>/',views.Update, name='update_task'),
    path('delete/<str:pk>/',views.Delete, name='delete')
]
