from django import forms

from django.contrib.auth.models import User

class RegisterForm(forms.Form): #registro de formularios 
    
    username = forms.CharField(required=True,
                                min_length=4, max_length=50,
                                widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username',
                                    'placeholder': 'Username'
                               }))
    email = forms.EmailField(required=True,
                            widget=forms.TextInput(attrs={
                                    'class': 'form-control',
                                    'id': 'email',
                                    'placeholder': 'example@sms.com'}))
    password = forms.CharField(required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control',
                                    'id': 'username',
                                    }))
    password2 = forms.CharField(label='Confirmar password',
                                required=True,
                                widget=forms.PasswordInput(attrs={
                                    'class': 'form-control'
                                }))

    def clean_username(self): # para validar un campo, en este caso es el username
        username = self.cleaned_data.get('username')

        if User.objects.filter(username=username).exists():
            raise forms.ValidationError('El username ya se encuentra en uso')

        return username


    def clean_email(self):
        email = self.cleaned_data.get('email')

        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('El email ya se encuentra en uso')

        return email

    def clean(self):#para validar campos que dependan uno de otro (en este caso los dos password)
        cleaned_data = super().clean()

        if cleaned_data.get('password2') != cleaned_data.get('password'):
            self.add_error('password2', 'El password no coincide')

    def save(self): # funcion encargada de crear usuarios
        return User.objects.create_user(
                self.cleaned_data.get('username'),
                self.cleaned_data.get('email'),
                self.cleaned_data.get('password'),
        )
