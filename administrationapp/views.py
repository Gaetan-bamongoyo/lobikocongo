from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.conf import settings
from django.core.mail import send_mail
from hopitalapp.models import *
from pharmacieapp.models import *
from .models import *
from bestsearchhospital.utils import *

# Create your views here.

def loginPage(request):
    return render(request, 'login/index.html')

@login_required
def dashboardPage(request):
    return render(request, 'admin/index.html')

@login_required
def logoutPage(request):
    logout(request)
    return redirect('administrationapp:home')
    
# @login_required
def hopitalPageCreate(request):
    return render(request, 'login/hopital.html') 

def createuser(request):
    user = CustomUser.objects.all()
    ville = Ville.objects.all()
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_pass = request.POST.get('confirme')
        compte = request.POST.get('compte') 
        if password==confirm_pass:
            if CustomUser.objects.filter(email=email).exists():
                message_erreur = 'Desole le compte existe deja'
                return render(request, 'login/index.html', {'message_erreur':message_erreur})
            else:
                form = CustomUser.objects.create_user(
                        username=username,
                        password=password,
                        email=email,
                        is_superuser = 0,
                        acces = compte,
                        first_name=username 
                    )
                form.set_password(password)
                form.save()
                user_id = form.id
                retrieved = CustomUser.objects.get(id=user_id)
                id = encrypt_id(retrieved.id)
                # message = render_to_string('login/email.html', {'user':retrieved})
                if compte == '1':
                    # send_mail(
                    #     'Bienvenu dans bestsearch',
                    #     message,
                    #     settings.DEFAULT_FROM_EMAIL,
                    #     [email]
                    # )
                    return render(request, 'login/hopital.html', {'user':id, 'ville':ville})
                else:
                    # send_mail(
                    #     'Bienvenu dans bestsearch',
                    #     'Merci de votre enregistrement,\n\n vous avez choisi la creation de compte pour votre hopital, veuillez clic sur ce lien ${http://127.0.0.1:8000/} pour completer les renseignements de votre hopital\n\n Cordialement!!!',
                    #     settings.DEFAULT_FROM_EMAIL,
                    #     [email]
                    # )
                    return render(request, 'login/pharmacie.html', {'user':id,  'ville':ville})
                # return render(request, 'login/message.html')
        else:
            return redirect('student:login')


def createhospital(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        designation = request.POST.get('designation')
        # getting province id
        ville = int(request.POST.get('ville'))
        ville_id = Ville.objects.get(id=ville)
        ville_id.id
        # end code
        adresse = request.POST.get('adresse')
        phone = request.POST.get('numero')
        numero = request.POST.get('enregistrement')
        consultation = request.POST.get('consultation')
        image = request.FILES.get('image')
        # decrypt id user
        id_pk = decrypt_id(pk)
        user_id = CustomUser.objects.get(id=id_pk)
        user_id.id
        # end code
        form = Hopital(
            designation = designation,
            ville = ville_id,
            adresse = adresse,
            numeroenregistrement = numero,
            phone = phone, 
            photo = image,
            is_active = True,
            consultation = consultation,
            user=user_id
        )
        form.save()
        return render(request, 'login/message.html')


def createpharmacie(request):
    if request.method == 'POST':
        pk = request.POST.get('id')
        designation = request.POST.get('designation')
        ville = int(request.POST.get('ville'))
        ville_id = Ville.objects.get(id=ville)
        ville_id.id
        phone = request.POST.get('phone')
        numeroenregistrement = request.POST.get('numeroenregistrement')
        adresse = request.POST.get('adresse')
        image = request.FILES.get('image')
        id_pk = decrypt_id(pk)
        user_id = CustomUser.objects.get(id=id_pk)
        user_id.id
        form = Pharmacie(
            designation=designation,
            numero_enregistrement=numeroenregistrement,
            ville=ville_id, 
            phone=phone,
            photo=image,
            adresse = adresse,
            user=user_id
        )
        form.save()
        return render(request, 'login/index.html')

def loginUser(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')    
        user = authenticate(username=username, password=password)
        if user is not None:
            auth_login(request, user)
            return redirect('administrationapp:homepage')
        else:
            return redirect('administrationapp:home')
    else:
        return render(request, '')

@login_required
def modifieruser(request):
    if request.user.is_authenticated:
        user_id = request.user.id
        if request.method=='POST':
            image = request.FILES.get('photo')
            user = CustomUser.objects.get(id=user_id)
            if not image:
                return redirect('/hospital/profil')
            else:
                form = CustomUser(
                    username=user.username,
                    password=user.password,
                    email=user.email,
                    is_superuser = user.is_superuser,
                    is_staff=user.is_staff,
                    first_name=user.first_name,
                    id=user.id,
                    photo=image
                )
                form.save()
                return redirect('/hospital/profil')


@login_required
def affichePage(request):
    return render(request,'superadmin/index.html')


@login_required
def affichePhamarcie(request):
    pharma = Pharmacie.objects.all()
    medoc = Medicament.objects.select_related('pharmacie','categorie')
    return render(request,'superadmin/pharmacie.html',{'medoc':medoc, 'pharma':pharma})

@login_required
def afficheHopital(request):
    hopital = Hopital.objects.all()
    quartier = Quartier.objects.all()
    equipements = Equipement.objects.select_related('choix__hopital')
    doc = Docteur.objects.select_related('choix__hopital')
    return render(request,'superadmin/hopital.html',{'hopital':hopital, 'equipements':equipements,'doc':doc,'quartier':quartier})

@login_required
def afficheEntreprise(request):
    services = Service.objects.all()
    context = {
        'services':services
    }
    return render(request,'superadmin/entreprise.html',context)
@login_required
def afficherProvince(request):
    province = Province.objects.all()
    return render(request,'superadmin/Province.html',{'province':province})
@login_required
def afficherVille(request):
    town = Province.objects.prefetch_related('ville_set')
    province = Province.objects.all()
    return render(request,'superadmin/ville.html',{'town':town, 'province':province})
@login_required
def afficherCommune(request):
    commune = Ville.objects.prefetch_related('commune_set')
    ville = Ville.objects.all()

    return render(request,'superadmin/commune.html',{'ville':ville, 'commune':commune})
@login_required
def afficherQuartier(request):
    quartier = Commune.objects.prefetch_related('quartier_set')
    commune = Commune.objects.all()
    return render(request,'superadmin/quartier.html',{'quartier':quartier , 'commune':commune})
@login_required
def afficherAvenue(request):
    avenue = Quartier.objects.prefetch_related('avenue_set')
    quartier = Quartier.objects.all()
    return render(request,'superadmin/avenue.html',{'avenue':avenue, 'quartier':quartier})



@login_required
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
        return redirect('administrationapp:entreprise')
@login_required
def createProvince(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        form = Province(
            designation = designation
        )
        form.save()
        return redirect('administrationapp:province')
       
@login_required
def createVille(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        province =int(request.POST.get('province'))
        ville_id = Province.objects.get(id = province)
        ville_id.id
        form = Ville(
            designation = designation,
            province = ville_id
        )
        form.save()
        return redirect('administrationapp:ville')
@login_required
def updateVille(request, pk):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        
        form = Ville(
            id = pk,
            designation = designation,
           
        )
        form.save()
        return redirect('administrationapp:ville')
def modifierVille(request, pk):
    ville = Ville.objects.get(id = pk)
    return render(request,'superadmin/ville.html',{'ville':ville})

@login_required
def createCommune(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        ville = int(request.POST.get('ville'))
        ville_id = Ville.objects.get(id = ville)
        ville_id.id
        form = Commune(
            designation = designation,
            ville_id = ville
        )
        form.save()
        return redirect('administrationapp:commune') 
@login_required
def ModifierCommune(request ,pk):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        ville = int(request.POST.get('ville'))
        ville_id = Ville.objects.get(id = ville)
        ville_id.id
        form = Commune(
            id = pk,
            designation = designation,
            ville_id = ville
        )
        form.save()
        return redirect('administrationapp:commune') 
def updateCommune(request, pk):
    communes = Commune.objects.get(id=pk)
    return render(request,'superadmin/commune.html')
def deletaCommune(request,pk):
    communes = Commune.objects.get(id=pk)
    communes.delete()
    return redirect('/admin/commune')
@login_required
def createQuartier(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        commune = int(request.POST.get('commune'))
        commune_id = Commune.objects.get(id = commune)
        commune_id.id
        form = Quartier(
            designation = designation,
            commune = commune_id
        )
        form.save()
        return redirect('administrationapp:quartier')
@login_required
def createAvenue(request):
    if request.method == 'POST':
        designation = request.POST.get('designation')
        quartier = int(request.POST.get('quartier'))
        quartier_id = Quartier.objects.get(id = quartier)
        quartier_id.id
        form = Avenue(
            designation = designation,
            quartier = quartier_id
        )
        form.save()
        return redirect('administrationapp:avenue')   
@login_required   
def deleteVille(request, pk):
    town = Ville.objects.get(id = pk)
    town.delete()
    return redirect('administrationapp:ville')