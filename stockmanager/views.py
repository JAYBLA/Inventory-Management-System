from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
import csv

from .forms import *
from .models import *

@login_required
def home(request):
    template_name = 'home.html'
    context ={}
    return render(request, template_name, context)

@login_required
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

@login_required
def delete_category(request, pk):
    template_name = 'delete_items.html'
    category = get_object_or_404(Category, id=pk)
    if request.method == 'POST':
        category.delete()
        return redirect(to='stockmanager:add_category')
    return render(request, template_name)

@login_required
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


@login_required
def list_item(request):
    template_name = 'list_item.html'
    items =Stock.objects.all()
    context ={
        'items':items,
        'heading':'Items List'
    }
    return render(request, template_name, context)

@login_required
def item_detail(request, pk):
    template_name = 'item_detail.html'
    item = get_object_or_404(Stock, id=pk)
    heading = item.item_name + '-' + 'Details'
    context = {
        "heading":heading,
        "item": item,
    }
    return render(request, template_name, context)

@login_required
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

@login_required
def delete_item(request, pk):
    template_name = 'delete_items.html'
    item = get_object_or_404(Stock, id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect(to='stockmanager:list_item')
    return render(request, template_name)


@login_required
def issue_items(request, pk):
    template_name = 'issue_item.html'
    item = get_object_or_404(Stock, id=pk)
    form = IssueItemForm(request.POST or None, instance=item)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity =instance.quantity-instance.issue_quantity
        #instance.issue_by = str(request.user)
        messages.success(request, "Issued SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name) + "s now left in Store")
        instance.save()
        
        return redirect('/item-detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())

    context = {
        "heading": 'Issue ' + str(item.item_name) + ' ' + 'Items',
        "item": item,
        "form": form,
        #"username": 'Issue By: ' + str(request.user),
    }
    return render(request, template_name, context)



@login_required
def receive_items(request, pk):
    template_name = 'receive_item.html'
    item = get_object_or_404(Stock, id=pk)
    form = ReceiveItemForm(request.POST or None, instance=item)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.quantity =instance.quantity + instance.receive_quantity
        instance.save()
        messages.success(request, "Received SUCCESSFULLY. " + str(instance.quantity) + " " + str(instance.item_name)+"s now in Store")

        return redirect('/item-detail/'+str(instance.id))
        # return HttpResponseRedirect(instance.get_absolute_url())
    context = {
            "heading": 'Receive ' + str(item.item_name) + ' ' + 'Items',
            "item": item,
            "form": form,
            #"username": 'Receive By: ' + str(request.user),
    }
    return render(request, template_name, context)

@login_required
def reorder_level(request, pk):
    template_name = 'reorder_level.html'
    item = get_object_or_404(Stock, id=pk)
    form = ReorderLevelForm(request.POST or None, instance=item)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, "Reorder level for " + str(instance.item_name) + " is updated to " + str(instance.reorder_level))

        return redirect("stockmanager:list_item")
    context = {
            "heading":'Add Reorder Level',
            "item": item,
            "form": form,
    }
    return render(request, template_name, context)
