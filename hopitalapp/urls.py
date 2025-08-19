from django.urls import path
from .views import *

app_name='hopitalapp' 
urlpatterns = [
    path('profil',profilPage,name='profil'),
    path('modifierhopital/<str:pk>', modifierHopital, name='modifierhopital'),
    path('service/<str:pk>', servicepage, name='service'),
    path('detail/<str:pk>', maladiepage, name='detail'),
    path('createservice/<str:pk>', createservicechoix, name='createservice'),
    path('createmaladie/<str:pk>', createmaladie, name='createmaladie'),
    path('createequipement/<str:pk>', createequipement, name='createequipement'),
    path('createmedecin/<str:pk>', createmedecin, name='createmedecin'),
    path('hopital/', hopitalCreation, name='hopital')
]
