from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm

@login_required(login_url=reverse_lazy('login'))
def profile_view(request):
    return render(request, 'app_auth/profile.html')


def login_view(request):
    redirect_url = reverse('profile')
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect(redirect_url)
        else:
            return render(request, 'app_auth/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)
        return redirect('profile')
    return render(request, 'app_auth/login.html', {'error': 'Пользователь не найден или пароль не верный'})


def register_view(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            print(form['username'].value)
            form.save()
            user = authenticate(request, username=form['username'].value(), password=form['password1'].value())
            login(request, user)
            url = reverse('profile')
            return redirect(url)
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'app_auth/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('main-page')
