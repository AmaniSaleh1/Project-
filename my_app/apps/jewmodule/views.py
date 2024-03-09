from django.shortcuts import render

def index(request):
    # Study the request
    return render(request, 'jewmodule/index.html')  # Rendering a template
