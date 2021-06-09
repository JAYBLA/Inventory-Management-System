from django import forms
from .models import Stock, Category

class StockCreateForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields =['category', 'item_name', 'quantity']
        

    
class CategoryCreateForm(forms.ModelForm):
  class Meta:
    model = Category
    fields = ['name']
