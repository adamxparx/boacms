from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from django.contrib.auth import logout
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomUserUpdateForm, ResidentForm

def auth_check(user):
    if user.is_authenticated:
        if user.role == 'resident':
            return redirect('dashboard')
        elif user.role == 'staff':
            return redirect('staff_dashboard')
    return None

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'
    def dispatch(self, request, *args, **kwargs):
        response = auth_check(request.user)
        if response:
            return response
        return super().dispatch(request, *args, **kwargs)
      
def index(request):
    user = request.user
    response = auth_check(user)
    if response:
        return response
    
    context = {
        'user': user,
    }
    return render(request, 'accounts/index.html', context)

def register(request):
    response = auth_check(request.user)
    if response:
        return response
    
    if request.method == 'POST':
        user_form = CustomUserCreationForm(request.POST)
        resident_form = ResidentForm(request.POST)
        if user_form.is_valid() and resident_form.is_valid():
            user = user_form.save()
            resident = resident_form.save(commit=False)
            resident.user = user
            resident.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login') 
    else:
        user_form = CustomUserCreationForm()
        resident_form = ResidentForm()

    context = {
        'user_form': user_form,
        'resident_form': resident_form,
    }
    return render(request, 'accounts/register.html', context)

@login_required
def dashboard(request):
    user = request.user

    if user.role == 'staff':
        return redirect('staff_dashboard')
    
    elif user.role == 'resident':

        context = {
            'user': user,
        }

        return render(request, 'accounts/dashboard.html', context)
    
    else:
        logout(request)
        messages.error(request, 'Invalid account. Please try again.')
        return redirect('login')

@login_required
def staff_dashboard(request):
    user = request.user
    if user.role == 'resident':
        return redirect('dashboard')
    return render(request, 'accounts/staff_dashboard.html')

@login_required
def profile(request):
    user = request.user
    
    if request.method == 'POST':
        form = CustomUserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User updated.')

    else:
        form = CustomUserUpdateForm(instance=user)

    context = {
        'form': form,
        'user': user,
    }
    return render(request, 'accounts/profile.html', context)