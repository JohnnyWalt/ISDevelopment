from django.shortcuts import render, redirect
from registration.forms import SignUpForm
from django.contrib import messages
from django.contrib.auth import login, authenticate, update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm

# Create your views here.
def signup(request):
    # POST requests are usually used for submissions
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            # redirect to the page where the user can see that his signing up was successful
            # in the urls.py has to be specified where to find the template that should be shown under:
            return redirect('/registration/done')
    else:
        form = SignUpForm()
        # definition of the folder where the signup.html template can be found
    return render(request, 'registration/signup.html', {'form': form})


def password_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important - otherwise user has to log in again
            messages.success(request, 'Your password was successfully updated!')
            return redirect('/registration/password_change/done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'registration/password_change.html', {'form': form})
