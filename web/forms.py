from django import forms

class ClienteForm(forms.Form):
    nombre = forms.CharField(label='Nombres',max_length=200,required=True)
    apellidos = forms.CharField(label='Apellidos',max_length=200,required=True)
    email = forms.EmailField(label='Email',required=True)
    direccion = forms.CharField(label='Dirección',widget=forms.Textarea)
    telefono = forms.CharField(label='Telefono',max_length=20)
