from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from administrationapp.models import *
from bestsearchhospital.utils import *
# Create your views here.

@login_required
def categoriePage(request):
    categorie = Categorie.objects.all()
    for i in categorie:
        i.encrypt_id = encrypt_id(i.id)
    return render(request, 'admin/categorie.html', {'categorie':categorie})

@login_required
def createcategorie(request):
    if request.method=='POST':
        designation = request.POST.get('designation')
        description = request.POST.get('description')
        form = Categorie(
            description=description,
            designation=designation
        )
        form.save()
        return redirect('/pharmacie/categorie')

@login_required
def medicamentPage(request, pk):
    decrypt = decrypt_id(pk)
    if request.user.is_authenticated:
        medicamentchoisie = MedicamentChoise.objects.select_related('medicament').filter(pharmacie=decrypt)
        medicament = Medicament.objects.all()
        return render(request, 'admin/medicament.html', {'medicament':medicament, 'medicamentchoisie':medicamentchoisie, 'pk':pk})


@login_required
def createmedicament(request, pk):
    if request.user.is_authenticated:
        id = request.user.id
        user_id = CustomUser.objects.get(id=id)
        pharmacie = Pharmacie.objects.get(user=id)
        pharmacie.id
        user_id.id
        if request.method=='POST':
            designation = request.POST.get('designation')
            description = request.POST.get('description')
            prix = request.POST.get('prix')
            image = request.FILES.get('image')
            medi = request.POST.get('medicament')
            retr = f'/pharmacie/medicament/{pk}'
            if medi.strip() == "":
                if Medicament.objects.filter(designation = designation).exists():
                    return redirect(retr)
                else:
                    formulaire = Medicament(
                        description = description,
                        designation = designation,
                        image = image
                    )
                    formulaire.save()
                    medicament_save = formulaire.id
                    found = Medicament.objects.get(id = medicament_save)
                    found.id
                    form_medicament = MedicamentChoise(
                        pharmacie=pharmacie,
                        prix=prix,
                        user=user_id,
                        medicament = found
                    )
                    form_medicament.save()
                    return redirect(retr)
            else:
                medicament = int(medi)
                medicament_id = Medicament.objects.get(id=medicament)
                medicament_id.id
                form = MedicamentChoise(
                    pharmacie=pharmacie,
                    prix=prix,
                    user=user_id,
                    medicament = medicament_id
                )
                form.save()
                return redirect(retr)
        else:
            return redirect(retr)
    return redirect(retr)

def pharmaciePage(request):
    pharmacie = Pharmacie.objects.all()
    for i in pharmacie:
        i.encrypt_id = encrypt_id(i.id)
    ville = Ville.objects.all()
    return render(request, 'admin/pharmacie.html', {'pharmacie':pharmacie,'ville':ville})
