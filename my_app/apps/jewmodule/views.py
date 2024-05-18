# views.py

from django.shortcuts import render, redirect, get_object_or_404
from .models import Jewelry
from .forms import JewelryForm

def index(request):
    return render(request, 'jewmodule/index.html')

def jewelry_list(request):
    jewelry_items = Jewelry.objects.all()
    return render(request, 'jewmodule/jewelryList.html', {'jewelry': jewelry_items})

def jewelry_detail(request, bId):
    obj = get_object_or_404(Jewelry, id=bId)
    return render(request, 'jewmodule/jewelry.html', {'jewelry': obj})

def add_jewelry(request):
    if request.method == 'POST':
        form = JewelryForm(request.POST)
        if form.is_valid():
            obj = form.save()
            return redirect('jewelry_detail', bId=obj.id)
    else:
        form = JewelryForm()
    return render(request, 'jewmodule/jewelryadd.html', {'form': form})

def update_jewelry(request, bId):
    obj = get_object_or_404(Jewelry, id=bId)
    if request.method == 'POST':
        form = JewelryForm(request.POST, instance=obj)
        if form.is_valid():
            obj = form.save()
            return redirect('jewelry_detail', bId=obj.id)
    else:
        form = JewelryForm(instance=obj)
    return render(request, 'jewmodule/updatejewelry.html', {'form': form})

def delete_jewelry(request, bId):
    obj = get_object_or_404(Jewelry, id=bId)
    obj.delete()
    return redirect('jewelry_list')

def filter_jewelry(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword', '').lower()
        is_title = request.POST.get('option1')
        is_type = request.POST.get('option2')

        if is_title and is_type:
            filtered_jewelry = Jewelry.objects.filter(
                title__icontains=keyword
            ) | Jewelry.objects.filter(
                type__icontains=keyword
            )
        elif is_title:
            filtered_jewelry = Jewelry.objects.filter(title__icontains=keyword)
        elif is_type:
            filtered_jewelry = Jewelry.objects.filter(type__icontains=keyword)
        else:
            filtered_jewelry = Jewelry.objects.all()
        
        return render(request, 'jewmodule/jewelryList.html', {'jewelry': filtered_jewelry})
    return render(request, 'jewmodule/search.html')
