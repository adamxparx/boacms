from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages
from .forms import CustomUserCreationForm
import re

# Create your views here.
def index(request):
    return render(request, 'accounts/index.html')

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True  # Optional: you can require email verification before activation
            user.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login')  # or wherever your login page is
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    # Retrieve user information to display on the dashboard
    context = {
        'user': request.user,
        # Add other context variables as needed
    }
    return render(request, 'accounts/dashboard.html', context)