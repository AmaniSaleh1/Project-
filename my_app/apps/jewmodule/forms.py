from django import forms
from .models import jewelry


class jewelryForm(forms.ModelForm):
    class Meta:
        model = jewelry 
        fields = ['title', 'type', 'price', 'edition']
        
    title = forms.CharField(
        max_length=100,
        required=True,
        label='Title',
        widget=forms.TextInput(
            attrs={
                'placeholder':'Enter the title here',
                'class':'mycssclass',
                'id':'myid',
            }
        )
    )
    author = forms.CharField(
        max_length=100,
        required=True,
        label='type'
    )
    
    price = forms.DecimalField(
        required=True,
        min_value= 1,
        max_value = 1000,
        label='Current Price'
    )
    
    edition = forms.IntegerField(
        required=True,
        label="Edition"
    )
        
    
