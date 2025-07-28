from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import *
from administrationapp.models import *
from bestsearchhospital.utils import *

# Create your views here. 
@login_required
def dashboardPage(request):
    return render(request, 'admin/index.html')

@login_required
def profilPage(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        hopital = Hopital.objects.get(user=user_id)
        crypt = encrypt_id(hopital.id)
        return render(request, 'admin/profil.html', {'hopital':hopital, 'id':crypt})

@login_required
def modifierHopital(request, pk):
    if request.user.is_authenticated:
        id = request.user.id
        id_pk = decrypt_id(pk)
        user_id = CustomUser.objects.get(id=id)
        user_id.id
        if request.method == 'POST':
            designation = request.POST.get('designation')
            adresse = request.POST.get('adresse')
            numero = request.POST.get('numero')
            image = request.FILES.get('image')
            phone = request.POST.get('phone')
            images = Hopital.objects.get(id=id_pk)
            if not image:      
                form = Hopital(
                    id=id_pk,
                    designation=designation,
                    adresse=adresse,
                    numero=numero,
                    phone=phone,
                    photo=images.photo,
                    user=user_id
                )
                form.save()
                return redirect('/hospital/profil')
            else:      
                form = Hopital(
                    id=pk,
                    designation=designation,
                    adresse=adresse,
                    numero=numero,
                    phone=phone,
                    photo=image,
                    user=user_id
                )
                form.save()
                return redirect('/hospital/profil')

@login_required
def servicepage(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        service = Service.objects.all()
        choix = ChoixService.objects.select_related('user', 'hopital', 'service').filter(user=user_id)
        for i in choix:
            i.encrypt_id = encrypt_id(i.id)
        context = {
            'service':service,
            'choix':choix
        }
        return render(request, 'admin/service.html', context)

@login_required
def maladiepage(request, pk):
    if request.user.is_authenticated:
        user_id = request.user.id
        id = decrypt_id(pk)
        choixservice = ChoixService.objects.get(id=id)
        crypt = encrypt_id(choixservice.id)
        maladie = Maladie.objects.select_related('choix__service', 'user').filter(choix=id)
        equipement = Equipement.objects.select_related('user').filter(choix=id)
        medecin = Docteur.objects.select_related('user').filter(choix=id)
        context = {
            'maladie':maladie,
            'choix': choixservice,
            'id': crypt,
            'equipement': equipement,
            'medecin': medecin
        }
        return render(request, 'admin/detailelement.html', context)

@login_required
def createservicechoix(request):
    if request.user.is_authenticated:
        id = request.user.id
        user_id = CustomUser.objects.get(id=id)
        user_id.id
        hopital = Hopital.objects.get(user=user_id)
        hopital.id
        if request.method=='POST':
            service = int(request.POST.get('service'))
            service_id = Service.objects.get(id=service)
            service_id.id
            # check = ChoixService.objects.get(user=user_id, hopital=hopital, service=service_id)
            # if check:
            form = ChoixService(
                hopital=hopital,
                user=user_id,
                service=service_id
            )
            form.save()
            return redirect('/hospital/service')
            # else:
            #     return redirect('/hospital/service')

@login_required
def createmaladie(request, pk):         
    if request.user.is_authenticated:
        id = request.user.id
        decrypt = decrypt_id(pk)
        user_id = CustomUser.objects.get(id=id)
        user_id.id
        choix = ChoixService.objects.get(id=decrypt)
        crypt = encrypt_id(choix.id)
        choix.id
        if request.method=='POST':
            maladie = request.POST.get('maladie')
            description = request.POST.get('description')
            
            form = Maladie(
                description=description,
                choix=choix,
                maladie=maladie, 
                user=user_id
            )
            form.save()
            url = f"/hospital/detail/{crypt}"
            return redirect(url)
            return render(request, 'admin/detailelement.html')

@login_required
def createequipement(request, pk):         
    if request.user.is_authenticated:
        id = request.user.id
        decrypt = decrypt_id(pk)
        user_id = CustomUser.objects.get(id=id)
        user_id.id
        choix = ChoixService.objects.get(id=decrypt)
        crypt = encrypt_id(choix.id)
        choix.id
        if request.method=='POST':
            designation = request.POST.get('designation')
            description = request.POST.get('description')
            prix = request.POST.get('prix')
            photo = request.FILES.get('image')
            
            form = Equipement(
                designation=designation,
                description=description,
                prix = prix,
                image=photo,
                choix=choix,
                user=user_id
            )
            form.save()
            url = f"/hospital/detail/{crypt}"
            return redirect(url)
            return render(request, 'admin/detailelement.html')


@login_required
def createmedecin(request, pk):         
    if request.user.is_authenticated:
        id = request.user.id
        decrypt = decrypt_id(pk)
        user_id = CustomUser.objects.get(id=id)
        user_id.id
        choix = ChoixService.objects.get(id=decrypt)
        crypt = encrypt_id(choix.id)
        choix.id
        if request.method=='POST':
            identite = request.POST.get('identite')
            numero = request.POST.get('numero_ordre')
            fonction = request.POST.get('fonction')
            photo = request.FILES.get('image')
            
            form = Docteur(
                identite=identite,
                fonction=fonction,
                numero = numero,
                image=photo,
                choix=choix,
                user=user_id
            )
            form.save()
            url = f"/hospital/detail/{crypt}"
            return redirect(url)
            return render(request, 'admin/detailelement.html')
