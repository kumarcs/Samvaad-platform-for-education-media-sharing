from django.shortcuts import render
from basicapp.forms import UserForm

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from basicapp.models import User_Table
from django.views.decorators.csrf import csrf_exempt

from django.db import connection



# Create your views here.

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@csrf_exempt
def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')





        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                print('Loginned' + username)
                n1 = User_Table.objects.filter(user_name__username__icontains=username)
                print(n1[0].type)
            if n1[0].type == 'InstitueAdmin':
                return HttpResponseRedirect(reverse('instituteAdmin'))
            elif n1[0].type == 'SuperAdmin':
                return HttpResponseRedirect(reverse('superAdmin'))
            elif n1[0].type == 'NormalUser':
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")
        else:
            print('someone tried login and failed')
            print('username : {} and password {}'.format(username, password))
            return HttpResponse("invalid comb of username password")
    else:
        return render(request, 'basicapp/login.html', {})

@login_required
def index(request):
    return render(request, 'basicapp/index.html')

@login_required
def instituteAdmin(request):
    return render(request, 'basicapp/instituteAdmin.html')


def superAdmin(request):
    return render(request, 'basicapp/superAdmin.html')
