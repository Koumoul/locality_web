from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import LoginForm, SigninForm

def home(request):
    return render(request, 'home/home.html')

def cultivateur_page(request):
    return render(request, 'home/cultivateur.html')

def proprietaire_page(request):
    return render(request, 'home/proprietaire.html')


def loginCultivateurView(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
    else:
        form = LoginForm()

    return render(request, 'home/login.html', locals())

def loginProprietaireView(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
        if user is not None and user.is_active:
            login(request, user)
        else:
            form = LoginForm()

    return render(request, 'home/login.html', locals())

def signinProprietaireView(request):

    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            family_name = form.cleaned_data["family_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]
            if password == password2:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                        last_name=family_name, email=email)
                user.save()
                group = Group.objects.get(name='Proprietaire')
                user.groups.add(group)
    else:
        form = SigninForm()

    return render(request, 'home/proprietaire.html', locals())


def signinCultivateurView(request):

    if request.method == "POST":
        form = SigninForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            family_name = form.cleaned_data["family_name"]
            username = form.cleaned_data["username"]
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]
            password2 = form.cleaned_data["password2"]
            if password == password2:
                user = User.objects.create_user(username=username, password=password, first_name=first_name,
                        last_name=family_name, email=email)
                user.save()
                group = Group.objects.get(name='Cultivateur')
                user.groups.add(group)
    else:
        form = SigninForm()

    return render(request, 'home/cultivateur.html', locals())

def signinView(request):
    form = SigninForm()
    return render(request, 'home/signin.html',locals())

def logoutView(request):

    logout(request)
    return HttpResponseRedirect('/home/signin')
