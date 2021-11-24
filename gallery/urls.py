from django.urls import path
from .import views

urlpatterns = [
    path('',views.gallerya,name='gallery',),
    path('photo/<str:pk>/',views.viewPhoto,name='photo',),
    path('add/',views.addPhoto,name='add',),

]