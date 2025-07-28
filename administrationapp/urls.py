from django.urls import path
from .views import *

app_name='administrationapp'
urlpatterns = [
    path('', loginPage ,name='home'),
    path('create', createuser, name='create'),
    path('createhopital', hopitalPageCreate, name='createhopital'),
    path('createpharmacie', createpharmacie, name='createpharmacie'),
    path('createhospital', createhospital, name='createhospital'),
    path('homepage', dashboardPage ,name='homepage'),
    path('login', loginUser,name='login'),
    path('modifieruser', modifieruser, name='modifieruser'),
    path('logout', logoutPage, name='logout'),

    path('accueil',affichePage,name='accueil'),
    path('pharmacie',affichePhamarcie,name='pharmacie'),
    path('hopital',afficheHopital,name='hopital'),
    path('entreprise',afficheEntreprise,name='entreprise'),
    path('createservice',createService,name='createservice'),
    path('province',afficherProvince,name='province'),
    path('ville',afficherVille,name='ville'),
    path('commune',afficherCommune,name='commune'),
    path('quartier',afficherQuartier,name='quartier'),
    path('avenue',afficherAvenue,name='avenue'),

    path('createprovince',createProvince,name='createprovince'),
    path('createville',createVille,name='createville'), 
    path('createcommune',createCommune,name='createcommune'),
    path('createquartier',createQuartier,name='createquartier'),
    path('createavenue',createAvenue,name='createavenue'),

    path('deleteville/<int:pk>',deleteVille, name='deleteville'),
    path('updateville/<int:pk>',updateVille, name='updateville'),
    path('modville/<int:pk>',modifierVille, name='modville'),
    path('delete/<int:pk>',deletaCommune,name='deletecommune'),
    path('modifier/<int:pk>', ModifierCommune, name='modifiercommune'),
    path('update/<int:pk>', updateCommune, name= 'updatecommune')


]
