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
    
class IssueItemForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['issue_quantity', 'issue_to']


class ReceiveItemForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['receive_quantity']
  
class ReorderLevelForm(forms.ModelForm):
	class Meta:
		model = Stock
		fields = ['reorder_level']
