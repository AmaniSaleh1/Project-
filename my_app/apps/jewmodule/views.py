<<<<<<< HEAD
from django.shortcuts import render,redirect

def index(request):
    # Study the request
    return render(request, 'jewmodule/index.html')  
# Rendering a template
def jewelry(request):
    u = request.user
    return render(request, 'jewmodule/jewelry.html') 

def jewelry(request, jew id):
    return None

def jewelry(request, bId):
    Gemstones1 = {'id': 12344321, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    Gemstones2 = {'id': 56788765, 'title': 'Reversing: Secrets of Reverse Engineering', 'author': 'E. Ellams'}
    
    target = None
    
    if Gemstones1['id'] == bId:
        targetBook = Gemstones1
    elif Gemstones2['id'] == bId:
        targetBook = Gemstones2
    
    context = {'book': targetBook}  # 'book'
    return render(request, 'jewmodule/book.html', context)

=======
<<<<<<< HEAD
from django.shortcuts import render

def index(request):
    # Study the request
    return render(request, 'jewmodule/index.html')  # Rendering a template
=======
from django.shortcuts import render

def index(request):
    # Study the request
    return render(request, 'jewmodule/index.html')  # Rendering a template
>>>>>>> f805db6a1790a2fd31e46ec097a587081675bc65
>>>>>>> 65a4a5d96c0f434d53e3290270e7c145a1ddb7f3
