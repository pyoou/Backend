from django.shortcuts import render, redirect

def index(request):
    return render(request, 'sensive/index.html')

def contact(request):
    return render(request, 'sensive/contact.html')

def category(request):
    return render(request, 'sensive/category.html')

def details(request):
    return render(request, 'sensive/blog-details.html')

def archive(request):
    return render(request, 'sensive/archive.html')