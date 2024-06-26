from django.shortcuts import render, redirect
from django.http import Http404
from .models import Jewelry
from .forms import JewelryForm, JewelryFilterForm
from django.views.decorators.csrf import csrf_exempt

def index(request):
    return render(request, 'jewmodule/index.html')

def jewelry_list(request):
    form = JewelryFilterForm(request.GET or None)
    jewelry_items = Jewelry.objects.all()

    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        type = form.cleaned_data.get('type')

        if keyword:
            jewelry_items = jewelry_items.filter(title__icontains=keyword)
        if min_price is not None:
            jewelry_items = jewelry_items.filter(price__gte=min_price)
        if max_price is not None:
            jewelry_items = jewelry_items.filter(price__lte=max_price)
        if type:
            jewelry_items = jewelry_items.filter(type__icontains=type)

    return render(request, 'jewmodule/jewelry_list.html', {'jewelry': jewelry_items, 'form': form})

def jewelry_detail(request, pk):
    try:
        obj = Jewelry.objects.get(pk=pk)
    except Jewelry.DoesNotExist:
        raise Http404("Jewelry not found")
    return render(request, 'jewmodule/jewelry_detail.html', {'jewelry': obj})

@csrf_exempt
def add_jewelry(request):
    if request.method == 'POST':
        form = JewelryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('jewelry_list')
    else:
        form = JewelryForm()
    return render(request, 'jewmodule/add_jewelry.html', {'form': form})

@csrf_exempt
def update_jewelry(request, pk):
    try:
        obj = Jewelry.objects.get(pk=pk)
    except Jewelry.DoesNotExist:
        raise Http404("Jewelry not found")
        
    if request.method == 'POST':
        form = JewelryForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('jewelry_list')
    else:
        form = JewelryForm(instance=obj)
    return render(request, 'jewmodule/update_jewelry.html', {'form': form})

@csrf_exempt
def delete_jewelry(request, pk):
    try:
        obj = Jewelry.objects.get(pk=pk)
    except Jewelry.DoesNotExist:
        raise Http404("Jewelry not found")
        
    if request.method == 'POST':
        obj.delete()
        return redirect('jewelry_list')
    return render(request, 'jewmodule/delete_jewelry.html', {'jewelry': obj})

# @csrf_exempt
def filter_jewelry(request):
    form = JewelryFilterForm(request.GET or None)
    jewelry_items = Jewelry.objects.all()

    if form.is_valid():
        keyword = form.cleaned_data.get('keyword')
        min_price = form.cleaned_data.get('min_price')
        max_price = form.cleaned_data.get('max_price')
        type = form.cleaned_data.get('type')

        if keyword:
            jewelry_items = jewelry_items.filter(title__icontains=keyword)
        if min_price is not None:
            jewelry_items = jewelry_items.filter(price__gte=min_price)
        if max_price is not None:
            jewelry_items = jewelry_items.filter(price__lte=max_price)
        if type:
            jewelry_items = jewelry_items.filter(type__icontains=type)

    return render(request, 'jewmodule/jewelry_list.html', {'jewelry': jewelry_items, 'form': form})
