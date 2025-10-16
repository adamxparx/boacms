from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView
from django.contrib import messages
from .forms import CustomUserCreationForm

def auth_check(user):
    if user.is_authenticated:
        if user.role == 'resident':
            return redirect('dashboard')
        elif user.role == 'barangay_staff':
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
    response = auth_check(request.user)
    if response:
        return response
    
    return render(request, 'accounts/index.html')

def register(request):
    response = auth_check(request.user)
    if response:
        return response

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been created successfully!')
            return redirect('login') 
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

@login_required
def dashboard(request):
    user = request.user

    if user.role == 'barangay_staff':
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
