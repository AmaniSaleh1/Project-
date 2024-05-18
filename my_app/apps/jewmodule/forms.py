from django import forms
from .models import Jewelry

class JewelryForm(forms.ModelForm):
    class Meta:
        model = Jewelry
        fields = ['title', 'type', 'price', 'edition']
        
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the title here',
                'class': 'mycssclass',
                'id': 'myid',
            }
        )
    )
    type = forms.CharField(
        max_length=100,
        required=True,
        label='Type',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Enter the type here',
                'class': 'mycssclass',
            }
        )
    )
    price = forms.DecimalField(
        required=True,
        min_value=1,
        max_value=1000,
        label='Current Price',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter the price here',
                'class': 'mycssclass',
            }
        )
    )
    edition = forms.IntegerField(
        required=True,
        label='Edition',
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Enter the edition here',
                'class': 'mycssclass',
            }
        )
    )
