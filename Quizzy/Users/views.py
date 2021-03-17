from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate, get_user_model
from .forms import LoginForm, RegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
# Create your views here.
User = get_user_model()

def login_view(request):
    login_form = LoginForm(request.POST or None)
    if login_form.is_valid():
        username = login_form.cleaned_data.get('username')
        password = login_form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Please Check Your Credentials Again !")
            return redirect('login')
    return render(request, 'Users/form.html', {'form':login_form})


def logout_view(request):
    logout(request)
    return render(request, 'Users/logout.html',{})

def register(request):
    register_form = RegisterForm(request.POST or None)
    if register_form.is_valid():
        usn = register_form.cleaned_data.get('username')
        email = register_form.cleaned_data.get('email')
        pwd1 = register_form.cleaned_data.get('password1')
        pwd2 = register_form.cleaned_data.get('password2')
        # user = User.objects.create_user(usn, email, pwd1)
        try:
            if pwd1 == pwd2:
                user = User.objects.create_user(usn, email, pwd1)
                messages.success(request, f'Account Created For {usn}!')
                return redirect('register')
            else:
                messages.error(request, "Please Check Your Credentials Again !")
        except:
            user = None
    return render(request, 'Users/signup.html',{'form':register_form})


@login_required
def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance = request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance = request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect('profile')
    user_form = UserUpdateForm(instance = request.user)
    profile_form = ProfileUpdateForm(instance = request.user.profile)
    return render(request, 'Users/profile.html', {'user_form':user_form, 'profile_form':profile_form})


# @login_required
# def profile(request):
#     return render(request, 'Users/profile.html', {})
