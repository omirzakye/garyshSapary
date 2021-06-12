import datetime
import json

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.sessions.backends import db
from django.http import HttpResponse, Http404, JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import CreateView, ListView, TemplateView
from .models import *
from .forms import *


def index(request):
    all_accounts = Account.objects.all()
    return render(request, "garysh\index.html", {"all_accounts": all_accounts})


def loginUser(request):
    if request.user.is_authenticated:
        return redirect('garysh:index')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('garysh:index')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'garysh\login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('garysh:index')


class registerView(CreateView):
    form_class = MyUserForm
    success_url = reverse_lazy('garysh:login')
    template_name = 'garysh\\registration.html'


def deleteUser(request, id):
    Account.objects.filter(id=id).delete()
    return redirect('garysh:index')


class UserUpdateView(UpdateView):
    model = Account
    fields = ['full_name', 'password']
    template_name = 'garysh\edit.html'
    success_url = reverse_lazy('garysh:login')
