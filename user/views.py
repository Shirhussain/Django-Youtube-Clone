from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm, UserUpdateForm, ChannelUpdateForm


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account hass been created for {username}')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'user/register.html', {'form': form})
    
@login_required
def channel(request):
    if request.method == "POST":
        uform = UserUpdateForm(request.POST, instance=request.user)
        cform = ChannelUpdateForm(request.POST, request.FILES, instance=request.user.channel)

        if uform.is_valid() and cform.is_valid():
            uform.save()
            cform.save()
            messages.success(request, 'your Account has been updateed ')
            return redirect('channel')
    else:
        uform = UserUpdateForm(instance=request.user)
        cform = ChannelUpdateForm(instance=request.user.channel)
        
    context = {
        'uform': uform,
        'cform':cform
    }
    return render(request, 'channel.html', context)
    


    # def search(request):
    #     pass


