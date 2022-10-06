from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.views.decorators.http import require_POST
from django.contrib.auth.forms import AuthenticationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context={
        'form':form,
    }
    return render(request, 'accounts/signup.html', context)
@require_POST
def logout(request):
    # 로그인 세션을 파기하는 과정
    # if request.method == "POST":
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect('accounts:index')
    # return redirect('accounts:login')
def login(request):
    if request.method == "POST":
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():         # 유저정보
            auth_login(request, form.get_user()) # 로그인!
            return redirect(request.Get.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form
    }
    return render(request, 'accounts/login.html', context)