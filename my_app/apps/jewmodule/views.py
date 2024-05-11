from django.shortcuts import render, redirect
from .models import jewelry
from .forms import jewelryForm

def index(request):
    # this view return index
	return render(request, 'jewmodule/index.html')

def jewelry(request):
    jewelry = jewelry.objects.all()
    return render(request, 'jewmodule/jewelryList.html', {'jewelry': jewelry})

def jewelry(request, bId): # read/sgiw/disply
    obj = jewelry.objects.get(id = bId)
    return render(request, 'jewmodule/jewelry.html', {'jewelry':obj})

def addjewelry(request):
    if request.method == 'POST':
        form = jewelryForm(request.POST)
        
        if form.is_valid():
            obj = form.save()
            return redirect('jewelry', bId = obj.id )
    form = jewelryForm(None)
    return render(request, "jewmodule/jewelryadd.html", {'form':form})

def updatejewelry(request, bId):
    obj = jewelry.objects.get(id = bId)
    if request.method == 'POST':
        form = jewelryForm(request.POST, instance=obj)
        if form.is_valid():
            obj.save()
            return redirect('jewelry', bId = obj.id )
        
    form = jewelryForm(instance=obj)
    return render(request, "jewmodule/updatejewelry.html", {'form':form})

def filterjewelry(request):
    
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        selected = request.POST.get('selectedgenre')
        
        myjew = jewelry.objects.filter(title__icontains='or')
        myjew2 = myjew.filter(price__lte = 100).exclude(author_icontains = 'j')
        
        print(f"selected thing = {selected}")
        # now filter
        jewelry = __getjewelry()
        newjewelry = []
        for item in jewelry:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            if contained: newBooks.append(item)       
        return render(request, 'jewodule/jewelryList.html', {'jewelry':newjewelry})
    return render(request, 'jewmodule/search.html', {})

    
