from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = {
            'first_name',
            'middle_name',
            'last_name',
        }

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        label='Email Address',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
    )

    first_name = forms.CharField(
        required=True,
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your first name'})
    )

    last_name = forms.CharField(
        required=True,
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your last name'})
    )

    middle_name = forms.CharField(
        required=False,
        label='Middle Name',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your middle name'})
    )

    date_of_birth = forms.DateField(
        required=True,
        label='Date of Birth',
        widget=forms.DateInput(attrs={'type': 'date'})
    )

    phone_number = forms.CharField(
        required=False,
        label='Phone Number',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )

    password1 = forms.CharField(
        required=True,
        label='Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}),
    )

    password2 = forms.CharField(
        required=True,
        label='Confirm Password',
        widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}),
    )

    class Meta:
        model = CustomUser
        fields = [
            'first_name',
            'last_name', 
            'middle_name',
            'date_of_birth',
            'email',
            'phone_number',
        ]

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and CustomUser.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already in use.")
        return phone_number
    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'resident'
        if commit:
            user.save()
        return user
