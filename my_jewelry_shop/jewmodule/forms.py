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
        max_value=10000,
        label='Price',
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

class JewelryFilterForm(forms.Form):
    keyword = forms.CharField(
        required=False,
        label='Search',
        widget=forms.TextInput(attrs={'placeholder': 'Enter keyword'})
    )
    min_price = forms.DecimalField(
        required=False,
        min_value=0,
        label='Min Price',
        widget=forms.NumberInput(attrs={'placeholder': 'Min Price'})
    )
    max_price = forms.DecimalField(
        required=False,
        min_value=0,
        label='Max Price',
        widget=forms.NumberInput(attrs={'placeholder': 'Max Price'})
    )
    type = forms.CharField(
        required=False,
        label='Type',
        widget=forms.TextInput(attrs={'placeholder': 'Type'})
    )

