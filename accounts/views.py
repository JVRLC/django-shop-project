from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model,login,authenticate
from django.contrib.auth import logout,login,get_user_model
# Create your views here.


User = get_user_model() #recup classe utilisateur

def signup(request):
    if request.method == "POST":
        # Traiter le formulaire
        username= request.POST.get("username")
        password= request.POST.get("password")
        user = User.objects.create_user(username=username,
                                 password=password)
        # connecter l'utilisateur
        login(request,user)
        return redirect('index')

    return render(request, 'accounts/signup.html')

def login_user(request):
    if request.method == "POST":
        # Connecter l'utilisateur
            username= request.POST.get("username")
            password= request.POST.get("password")
            user = authenticate(request, username=username, password=password)
            if user:
                login(request,user)
                return redirect('index')
            
    return render(request, "accounts/login.html")


def logout_user(request):
    logout(request)
    return redirect('index')
