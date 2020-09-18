from django.shortcuts import render, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth import logout, login, authenticate
from .forms import LoginForm, RegistrationForm


def login_view(request):
    template = 'form.html'
    form = LoginForm(request.POST or None)

    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)
        login(request, user)
        return HttpResponse("login successful!")
        
    context = {
        "form": form
    }

    return render(request, template, context)


def registration_view(request):
    template = 'form.html'
    form = RegistrationForm(request.POST or None)

    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.save()
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)
        # login(request, user)
        # return HttpResponse("login successful!")
        
    context = {
        "form": form
    }

    return render(request, template, context)