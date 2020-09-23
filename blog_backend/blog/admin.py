from django.contrib import admin

from .models import Article, Category, Person

admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Person)