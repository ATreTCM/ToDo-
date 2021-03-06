from django.shortcuts import render
from .forms import UserRegistrationForm
from django.contrib.auth.models import User


def register(request):
    """Регистрация пользователей"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})


def userList(request):
    """список зарегистрированых пользователей"""
    users_list = User.objects.all()
    context = {
        'users_list': users_list,
        'section': 'dashboard',
    }
    return render(request, 'account/dashboard.html', context)
