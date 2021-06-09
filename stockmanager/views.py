from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import csv

from .forms import StockCreateForm, CategoryCreateForm
from .models import Stock, Category

def home(request):
    template_name = 'home.html'
    context ={}
    return render(request, template_name, context)

def add_category(request):
    template_name = 'add_category.html'
    categories =Category.objects.all()
    if request.POST:
        form = CategoryCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(to='stockmanager:add_category')
    else:
        form = CategoryCreateForm()
    context ={
        'form':form,
        'categories':categories,
        'heading':'Category List',
    }
    return render(request, template_name, context)

def delete_category(request, pk):
    template_name = 'delete_items.html'
    category = get_object_or_404(Category, id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect(to='stockmanager:add_category')
    return render(request, template_name)

def add_item(request):
    template_name = 'add_item.html'
    if request.POST:
        form = StockCreateForm(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect(to='stockmanager:list_item')
    else:
        form = StockCreateForm()
    context ={'form':form}
    return render(request, template_name, context)


def list_item(request):
    template_name = 'list_item.html'
    items =Stock.objects.all()
    context ={
        'items':items,
        'heading':'Items List'
    }
    return render(request, template_name, context)

def update_item(request,pk):
    template_name = 'add_item.html'
    item =get_object_or_404(Stock, id=pk)
    if request.POST:
        form = StockCreateForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect(to='stockmanager:list_item')
    else:
        form = StockCreateForm(instance=item)
    context = {
        'form':form
    }
    return render(request, template_name, context)

def delete_item(request, pk):
    template_name = 'delete_items.html'
    item = get_object_or_404(Stock, id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect(to='stockmanager:list_item')
    return render(request, template_name)
