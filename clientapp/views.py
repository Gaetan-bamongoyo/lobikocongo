from django.shortcuts import render
from pharmacieapp.models import *
from hopitalapp.models import *
from bestsearchhospital.utils import *
# Create your views here.
def clientPage(request):
    return render(request,'client/index.html')

def affiche_template(request):
    return render(request,'client/structure.html')

def affiche_service(request):
    service = Service.objects.all()
    for i in service:
            i.encrypt_id = encrypt_id(i.id)
    return render(request,'client/service.html',{"service":service})

def affiche_pharmacie(request):
    medoc = Medicament.objects.all()
    for i in medoc:
            i.encrypt_id = encrypt_id(i.id)
    return render(request,'client/pharmacie.html',{"medoc":medoc})

def detailafficheservice(request, pk):
    id = decrypt_id(pk)
    pharmacie = MedicamentChoise.objects.select_related('pharmacie').filter(medicament__id = id)
    for i in pharmacie:
            i.encrypt_id = encrypt_id(i.id)
    ville = Ville.objects.all()
    return render(request,'client/lespharmacies.html',{"pharmacie":pharmacie, "ville":ville})

def affiche_hopital(request):
    hopital = Hopital.objects.select_related('ville')
    for i in hopital:
            i.encrypt_id = encrypt_id(i.id)
    return render(request,'client/hopital.html',{'hopital':hopital})

def detailhopitalPage(request, pk):
    id = decrypt_id(pk)
    hopital = Hopital.objects.prefetch_related('choixservice__equipement','choixservice__docteur').get(id = id)
    return render(request, 'client/detailhopital.html', {'hopital':hopital})

def servicehopitalPage(request, pk):
    id = decrypt_id(pk)
    hopital = Hopital.objects.filter(choixservice__service__id = id).distinct()
    for i in hopital:
            i.encrypt_id = encrypt_id(i.id)
    return render(request, 'client/service_hopital.html', {'hopital':hopital})