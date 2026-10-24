from django import forms
from .models import Avtomobil

class AvtomobilForm(forms.ModelForm):
    class Meta:
        model = Avtomobil
        fields = [
            'marka', 'model', 'il', 'qiymet', 'valyuta', 
            'muherrik', 'yurush', 'seher', 'telefon', 'kredit', 'barter', 'yeni', 'shekil'
        ]