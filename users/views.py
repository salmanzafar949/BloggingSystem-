from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm

def register(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            # password = form.cleaned_data.get('password')
            messages.success(request, f'Account created for {username}..!')
            return redirect('blog:index')
    else:
        form = UserForm()
    return render(request, 'users/register.html', {'form': form})
