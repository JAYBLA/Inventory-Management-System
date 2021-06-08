from django.shortcuts import render,redirect
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
        items = Stock.objects.filter(category__iexact=form['category'].value(),
                                    item_name__iexact=form['item_name'].value()
                                    )
    print('items:',items)
    context = {
    "form": form,
    'heading':'Items List',
    'items':items,
    }
    return render(request, template_name, context)