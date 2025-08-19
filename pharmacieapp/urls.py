from django.urls import path
from .views import *

app_name='pharmacieapp'
urlpatterns = [
    path('categorie', categoriePage, name='categorie'),
    path('createcategorie', createcategorie, name='createcategorie'),
    path('medicament/<str:pk>', medicamentPage, name='medicament'),
    path('createmedicament/<str:pk>', createmedicament, name='createmedicament'),
    path('pharmacie', pharmaciePage, name='pharmacie')
]
