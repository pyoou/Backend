from django.db import models


class Category(models.Model):

    title = models.CharField(max_length=40)
    
    def __str__(self):
        return "%s" % (self.title)


class Article(models.Model):

    title   = models.CharField(max_length=100)
    content = models.TextField()
    author  = models.CharField(max_length=40)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "#%s, %s" % (self.id, self.title) 

    
    class Meta:
        ordering = ['title', 'created_at', 'category']