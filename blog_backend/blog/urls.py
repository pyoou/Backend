from django.urls import path

from .apiviews import ArticleAPI, APIs
from . import blogviews

urlpatterns = [
    path('dev/api/', ArticleAPI.as_view()),
    path('dev/api/<int:id>/', ArticleAPI.as_view()),

    path('dev/apis/', APIs.as_view()),



    path('', blogviews.index, name='index'),
    path('contact/', blogviews.contact, name='contact'),
    path('category/', blogviews.category, name='category'),
    path('details/', blogviews.details, name='details'),
    path('archive/', blogviews.archive, name='archive'),
]