# forms.py
from django import forms
from .models import Entry

class EntryForm(forms.ModelForm):
    class Meta:
        model  = Entry
        fields = ['last_name', 'first_name', 'program', 'email', 'phone', 'score']
        widgets = {
            'phone': forms.TextInput(attrs={'placeholder': '+7 (___) ___-__-__'}),
        }
