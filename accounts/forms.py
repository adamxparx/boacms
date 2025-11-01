from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Resident

class CustomUserUpdateForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = {
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'sex',
            'address',
            'phone_number',
            'civil_status',
            'citizenship',
        }

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = [
            'email',
            'password1',
            'password2',
        ]

    email = forms.EmailField(
        required=True,
        label='Email Address',
        widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'})
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

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if CustomUser.objects.filter(email=email).exists():
            raise forms.ValidationError("This email address is already registered.")
        return email

    
    def save(self, commit=True):
        user = super().save(commit=False)
        user.role = 'resident'
        if commit:
            user.save()
        return user

class ResidentForm(forms.ModelForm):
    class Meta:
        model = Resident
        fields = [
            'first_name',
            'middle_name',
            'last_name',
            'date_of_birth',
            'address',
            'phone_number',
            'sex',
            'civil_status',
            'citizenship',
        ]
    
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

    address = forms.CharField(
        required=True,
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your address'})
    )

    phone_number = forms.CharField(
        required=False,
        label='Phone Number',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your phone number'})
    )

    citizenship = forms.CharField(
        required=True,
        label='Citizenship',
        widget=forms.TextInput(attrs={'placeholder': 'Enter your nationality'})
    )

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if phone_number and Resident.objects.filter(phone_number=phone_number).exists():
            raise forms.ValidationError("This phone number is already in use.")
        return phone_number