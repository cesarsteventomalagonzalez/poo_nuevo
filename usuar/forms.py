from django import forms
from django.forms import ModelForm
from usuar.models import *

class PostulanteForm(ModelForm):
    class Meta:
        model = Postulante
        fields = '__all__'
        widgets = {
            'nombres': forms.TextInput(attrs={'placeholder':'Ingrese Nombres','class': 'form-control','placeholder':'Ingrese Nombres','required':True }),
            'apellidos':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese Apellidos','required':True }),
            'email':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese correo','required':True,'type':'email' }),
            'telefonos':forms.TextInput(attrs={'class': 'form-control','placeholder':'Ingrese de telefono','required':True, 'type':'number' }),
            
            }
