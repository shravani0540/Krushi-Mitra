from django.urls import path
from .import views

urlpatterns = [
    path('', views.index, name='index'),
    path('second/', views.second, name='second'),
    path('third/', views.third, name='third'),
    path('fourth/', views.fourth, name='fourth'),
    path('fifth/', views.fifth, name='fifth'),
    path('sixth/', views.sixth, name='sixth'),
    path('seventh/', views.seventh, name='seventh'),
]