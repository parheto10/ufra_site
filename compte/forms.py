from django import forms

class LoginForm(forms.Form):
	username = forms.CharField(label="Nom Utilisatuer")
	password = forms.CharField(label="Mot de Passe", widget=forms.PasswordInput)