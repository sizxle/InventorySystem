from itertools import product

from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'
        labels = {
            'product_id' : 'Product ID',
            'name' : 'Name',
            'sku' : 'SKU',
            'price' : 'Price',
            'quantity' : 'Quantity',
            'supplier' : 'Supplier',
        }
        widgets = {
            'product_id' : forms.NumberInput(attrs={'class':'form-control','placeholder':'e.g. 1'}),
            'name' : forms.TextInput(attrs={'class':'form-control' ,'placeholder':'e.g. shirt '}),
            'sku' : forms.TextInput(attrs={'class': 'form-control' ,'placeholder':'e.g. S12345'}),
            'price' : forms.NumberInput(attrs={'class':'form-control','placeholder':'e.g. 19.99'}),
            'quantity' : forms.NumberInput(attrs={'class':'form-control','placeholder':'e.g. 10'}),
            'supplier' : forms.TextInput(attrs={'class':'form-control','placeholder':'e.g. Molefi Holdings'}),
        }

