from django.db import models


class Person(models.Model):

    name        = models.CharField(max_length=20)
    surname     = models.CharField(max_length=20)
    login       = models.CharField(max_length=20)
    password    = models.CharField(max_length=20)
    email       = models.EmailField()
    phone       = models.IntegerField()
    date        = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return "%s: %s%s" % (self.id, self.surname[:1],self.name[:1])

    class Meta:
        ordering = ['id', 'surname', 'date']





class Category(models.Model):

    title = models.CharField(max_length=40)
    
    def __str__(self):
        return "%s" % (self.title)


class Article(models.Model):

    title       = models.CharField(max_length=100)
    content     = models.TextField()
    author      = models.CharField(max_length=40)
    tags    = models.CharField(max_length=10)

    created_at  = models.DateTimeField(auto_now_add=True)
    updated_at  = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "#%s, %s" % (self.id, self.title) 

    
    class Meta:
        ordering = ['title', 'created_at', 'category']