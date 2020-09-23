from django.shortcuts import render, redirect
from rest_framework import generics as gen
from rest_framework import mixins as mix
from rest_framework.authentication import (BasicAuthentication,
                                           SessionAuthentication)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Article
from .serializers import ArticleSerializer


class APIs(APIView):

    queryset = Article.objects.all()


    def get(self, request, format=None):
        try:
                articles = [(article.id, article.title, article.date) for article in Article.objects.all()]
                return Response(articles)
            
        except:
                return redirect('dev')



class ArticleAPI(gen.ListCreateAPIView, mix.ListModelMixin, mix.CreateModelMixin, mix.UpdateModelMixin, mix.RetrieveModelMixin, mix.DestroyModelMixin):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

    def get(self, request, id=None):
        
        if id:
            return self.retrieve(request)
        
        else:
            return self.list(request)
        
        return self.list(request)

    def post(self, request):

        return self.create(request)

    def put(self, request, id=None):

        return self.create(request)

    def delete(self, request, id):
        return self.destroy(request, id)


'''
 #authentication_classes = [SessionAuthentication, BasicAuthentication]
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
'''
