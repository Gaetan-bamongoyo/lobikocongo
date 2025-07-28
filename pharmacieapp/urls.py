from django.urls import path
from .views import *

app_name='pharmacieapp'
urlpatterns = [
    path('categorie', categoriePage, name='categorie'),
    path('createcategorie', createcategorie, name='createcategorie'),
    path('medicament', medicamentPage, name='medicament'),
    path('createmedicament', createmedicament, name='createmedicament')
]
