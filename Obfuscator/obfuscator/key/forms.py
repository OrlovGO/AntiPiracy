from django import forms


class KeyForm(forms.Form):
    key_field = forms.CharField(widget=forms.TextInput)
    ID_field = forms.CharField(widget=forms.TextInput)


class LoginForm(forms.Form):
    login_field = forms.CharField(widget=forms.TextInput)