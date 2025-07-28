from django.shortcuts import render , redirect
from administrationapp.models import *
from pharmacieapp.models import *
from hopitalapp.models import *
# Create your views here.

def indexPage(request):
    return render(request,'superadmin/structure.html')
def affichePage(request):
    return render(request,'superadmin/index.html')
def affichePhamarcie(request):
    pharma = Pharmacie.objects.all()
    medoc = Medicament.objects.select_related('pharmacie','categorie')
    
    return render(request,'superadmin/pharmacie.html',{'medoc':medoc, 'pharma':pharma})
def afficheHopital(request):
    hopital = Hopital.objects.all()
    equipements = Equipement.objects.select_related('choix__hopital')
    doc = Docteur.objects.select_related('choix__hopital')
    
    return render(request,'superadmin/hopital.html',{'hopital':hopital, 'equipements':equipements,'doc':doc})

def afficheEntreprise(request):
    services = Service.objects.all()
    context = {
        'services':services
    }
    return render(request,'superadmin/entreprise.html',context)


def createService(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        description = request.POST.get('description')
        icon = request.POST.get('icon')
        form = Service(
            designation = designation,
            description = description,
            icon = icon
        )
        form.save()
        return redirect('app:entreprise')
def afficherProvince(request):
    return render(request,'superadmin/province.html')