from django import forms

class Servicio_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    presentacion = forms.IntegerField()

class Cliente_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    cuit = forms.IntegerField()

class Profesional_formulario(forms.Form):
    
    nombre = forms.CharField(max_length=20)
    cuit = forms.IntegerField()
