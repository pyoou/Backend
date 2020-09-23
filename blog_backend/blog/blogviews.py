from django.shortcuts import render, redirect
from .models import Article, Category


def index(request):

    articles = Article.objects.order_by('-updated_at')

    categories = Category.objects.all()

    context = {'articles' : articles, 'categories' : categories}

    return render(request, 'sensive/index.html', context)

def contact(request):
    return render(request, 'sensive/contact.html')

def category(request):
    return render(request, 'sensive/category.html')

def details(request):
    return render(request, 'sensive/blog-details.html')

def archive(request):
    return render(request, 'sensive/archive.html')