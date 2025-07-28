from django.urls import path
from .views import *

app_name = 'app'
urlpatterns = [
   
    path('',affichePage,name='accueil'),
    path('pharmacie',affichePhamarcie,name='pharmacie'),
    path('hopital',afficheHopital,name='hopital'),
    path('entreprise',afficheEntreprise,name='entreprise'),
    path('createservice',createService,name='createservice'),
    path('province',afficherProvince,name='province')
]