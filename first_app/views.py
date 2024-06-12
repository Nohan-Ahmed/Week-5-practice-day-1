from django.shortcuts import render, redirect
from first_app import forms
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, SetPasswordForm
from django.contrib.auth import login, logout, authenticate, update_session_auth_hash


# Create your views here.
def profile(req):
    if req.user.is_authenticated:
        if req.method == 'POST':
            form = forms.UpdateProfile(req.POST, instance=req.user)
            if form.is_valid():
                user = form.save()
                return redirect('profile')
        else:
            form = forms.UpdateProfile(instance=req.user)
        return render(req, './profile.html', {'form': form})
    else:
        return redirect('login')


def singup(req):
    if not req.user.is_authenticated:
        if req.method == 'POST':
            form = forms.Singup(req.POST)
            if form.is_valid():
                form.save()
                messages.success(request=req,
                                 message='Account created successfully.')
                return redirect('login')
        else:
            form = forms.Singup()
        return render(req, './singup.html', {'form': form})
    else:
        return redirect('profile')


def user_login(req):
    if not req.user.is_authenticated:
        if req.method == 'POST':
            form = AuthenticationForm(request=req, data=req.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(req, user)
                    return redirect('profile')
        else:
            form = AuthenticationForm()
        return render(req, './login.html', {'form': form})
    else:
        return redirect('profile')


def user_logout(req):
    logout(request=req)
    return redirect('login')

def change_pass(req):
    if req.method=='POST':
        form = PasswordChangeForm(user=req.user, data= req.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(req, form.user)
            return redirect('profile')
    else:
        form = PasswordChangeForm(req.user)
    return render(req, './change_pass.html', {'form': form})