from django.shortcuts import render, redirect
from .models import jewelry

def index(request):
    # this view return index
	return render(request, 'jewmodule/index.html')

def jewelry(request):
    jewelry = jewelry.objects.filter(price__lte = 100).order_by('-price')
    print(str(len(jewelry)))
    return render(request, 'jewmodule/jeList.html', {'jewelry': jewelry})

def filter_jewelry(request):
    
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        
        selected = request.POST.get('selectedgenre')
        
        my_jewelry = jewelry.objects.filter(title__icontains='or')
        my_jewelry2 = my_jewelry.filter(price__lte = 100).exclude(author_icontains = 'Am')
        
        print(f"selected thing = {selected}")
        # now filter
        jewelry = getjewelry()
        news = []
        for item in jewelry:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower(): contained = True
            if contained: news.append(item)       
        return render(request, 'jewmodule/bookList.html', {'books':news})
    return render(request, 'jewmodule/search.html', {})

def jewelry(request, bId):
    
    jewelry1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    jewelry2 = {'id':56788765, 'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    
    targetBook = None
    if jewelry1['id'] == bId: target = jewelry1
    if jewelry2['id'] == bId: target = jewelry2
    
    if target == None: return redirect('/jewelry')
    
    context = {'j':targetBook} # book is the variable name accessible by template
    return render(request, 'jewmodule/j.html', context)