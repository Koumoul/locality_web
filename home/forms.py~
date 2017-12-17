from django import forms

class LoginForm(forms.Form):

    username = forms.CharField(label="Username", max_length=30)
    password = forms.CharField(label="Password", widget=forms.PasswordInput)

class SigninForm(forms.Form):
    first_name = forms.CharField(label="Prenom", max_length=30)
    family_name = forms.CharField(label="Nom de famille", max_length=30)
    email = forms.EmailField(label="Email")
    password = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password (again)", widget=forms.PasswordInput)
    username = forms.CharField(label="Surnom", max_length=30)

