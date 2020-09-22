from django.urls import path

from .views import ArticleAPI

urlpatterns = [
    path('dev/api/', ArticleAPI.as_view()),
    path('dev/api/<int:id>/', ArticleAPI.as_view()),
]