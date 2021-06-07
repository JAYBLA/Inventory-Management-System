from django.shortcuts import render,redirect
from .forms import StockCreateForm
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
    items =Stock.objects.all()
    context ={
        'items':items,
        'heading':'Items List'
    }
    return render(request, template_name, context)