from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login,logout,authenticate
from django.shortcuts import render
from .models import Serie



#view de nos film
#def series_view(request):
    #series = Serie.objects.all()
   # return render(request, 'estiamflix/home.html', {'series': series})

def home(request):
    return render(request, 'estiamflix/home.html', {'form': UserCreationForm()})

def signupuser(request):
    if request.method == 'GET':
     return render(request,'estiamflix/signupuser.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
         try:
            user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
            user.save()
            login(request,user)
            return redirect('actuelestiamflix')
         except IntegrityError:
            return render(request, 'estiamflix/signupuser.html', {'form': UserCreationForm(), 'error': 'Nom d utilisateur deja utilise'})
         else:
            return render(request, 'estiamflix/signupuser.html',{'form': UserCreationForm(),'error':'Verifiez que vous avez bien saisie le mdp'})

def loginuser(request):
    if request.method == 'GET':
     return render(request,'estiamflix/login.html',{'form':AuthenticationForm()})

    else:
     user = authenticate(request,username=request.POST['username'],password=request.POST['password'])
     if user is None:
       return render(request,'estiamflix/login.html',{'form':AuthenticationForm(),'error':'Nom d utilisateur ou mdp incorrect'})
     else:
      login(request,user)
      return redirect('actuelestiamflix')


def logoutuser(request):
    if request.method =='POST':
        logout(request)
        return redirect('home')
def actuelestiamflix(request):
    return render(request, 'estiamflix/actuelestiamflix.html')


#view de nos film
def series_view(request):
    series = Serie.objects.all()
    return render(request, 'estiamflix/home.html', {'Serie': series})
    return render(request, 'estiamflix/home.html', {'Serie': series})
