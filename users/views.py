from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            messages.success(request, f'Your account has been created..!please login now..!')
            return redirect('users:login')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})
@login_required()
def userprofile(request):
    return render(request, 'users/profile.html')