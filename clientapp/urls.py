from django.urls import path
from .views import *

app_name='clientapp'
urlpatterns =[
    path('',clientPage,name='accueil'),
    path('hopital',affiche_hopital,name='hopital'),
    path('affiche',affiche_template,name='affiche'),
    path('pharmacie',affiche_pharmacie,name='pharmacie'),
    path('hopital_item/<pk>', detailhopitalPage, name='hopital_item'),
    path('service', affiche_service, name='service'),
    path('detailservice/<pk>', servicehopitalPage, name='detailservice'),
    path('lespharmacie/<pk>', detailafficheservice, name='lespharmacie')
]