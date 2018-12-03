from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserForm, UpdateForm, ProfileForm
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
    if request.method == "POST":
        userupdateform = UpdateForm(request.POST, instance=request.user)
        profileform = ProfileForm(request.POST,
                                  request.FILES,
                                  instance=request.user.profile)
        if userupdateform.is_valid() and profileform.is_valid():
            userupdateform.save()
            profileform.save()
            messages.success(request, f'Your profile has been updated..!')
            return redirect('users:profile')
        else:
            pass
    else:
        userupdateform = UpdateForm(instance=request.user)
        profileform = ProfileForm(instance=request.user.profile)

    context = {
        'u_form': userupdateform,
        'p_form': profileform
    }

    return render(request, 'users/profile.html', context)
