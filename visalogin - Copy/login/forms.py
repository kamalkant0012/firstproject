from tkinter.ttk import Widget
from attr import attr, fields
from django import forms
from login.models import emplogin
class empform(forms.ModelForm):
    class Meta:
        model=emplogin
        fields='__all__'
        widgets = {
            'name':forms.TextInput(attrs={'class':'form-control','placeholder':'Name'}),
            'passportid':forms.TextInput(attrs={'class':'form-control','placeholder':'Id Number'}),
        }