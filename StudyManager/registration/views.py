from django.shortcuts import render, redirect
from registration.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# import win32api

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # return win32api.MessageBox(0, 'The registration was successful!', 'Congratulations!') and 
            return redirect('/')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important! otherwise user has to log in again
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/registration/password_change/done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {'form': form})
