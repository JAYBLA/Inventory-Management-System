from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
import csv

from .forms import StockCreateForm, StockSearchForm
from .models import Stock

def home(request):
    template_name = 'home.html'
    context ={}
    return render(request, template_name, context)


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
    form = StockSearchForm(request.POST or None)
    items =Stock.objects.all()
    context ={
        "form": form,
        'items':items,
        'heading':'Items List'
    }
    if request.method == 'POST':
        items = Stock.objects.filter(
            category__icontains=form['category'].value(),
            item_name__icontains=form['item_name'].value()
        )
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="List of stock.csv"'
            writer = csv.writer(response)
            writer.writerow(['CATEGORY', 'ITEM NAME', 'QUANTITY'])
            instance = items
            for stock in instance:
             writer.writerow([stock.category, stock.item_name, stock.quantity])
            return response
        context = {
        "form": form,
        'heading':'Items List',
        'items':items,
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
