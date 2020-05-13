from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from registration.forms import SignUpForm
import win32api

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
            return win32api.MessageBox(0, 'The registration was successful!', 'Congratulations!') and redirect('../home/')

    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})