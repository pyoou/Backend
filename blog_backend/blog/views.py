from django.shortcuts import render

from rest_framework import generics as gen
from rest_framework import mixins as mix

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated

from .models import Article
from .serializers import ArticleSerializer


class ArticleAPI(gen.GenericAPIView, mix.ListModelMixin, mix.CreateModelMixin, mix.UpdateModelMixin, mix.RetrieveModelMixin, mix.DestroyModelMixin):
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