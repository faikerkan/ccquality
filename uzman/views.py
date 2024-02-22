from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Degerlendirme
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required


def dashboard_uzman_view(request):
    return render(request, 'dashboard_uzman.html')


@login_required
def degerlendirme_uzman_view(request):
    return render(request, 'degerlendirme_uzman.html')


def redirect_to_login(request):
    return redirect('/login/')


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # Kullanıcıya göre yönlendirme
                if user.is_staff:  # Doğru özellik ismiyle kontrol
                    return redirect('/dashboard/uzman/')
                else:
                    return redirect('/dashboard/genel/')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})