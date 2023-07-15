from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import BookModel,AuthorModel,BookCategory
from .serializer import BookSerializer,AuthorSerializer,BookCategorySerializer
from .permissions import IsOwnerPermissions

# Create your views here.
class ListCreateBookView(generics.ListCreateAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsAuthenticated,)

class DetailUpdateDeleteBookView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookModel.objects.all()
    serializer_class = BookSerializer
    permission_classes = (IsOwnerPermissions,)

# AuthorModel CRUD ---------------------------------------------
class ListCreatAuthorView(generics.ListCreateAPIView):
    queryset = AuthorModel.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = (IsAuthenticated,)

class DetailUpdateDeleteAuthorView(generics.RetrieveUpdateDestroyAPIView):
    queryset = AuthorModel.objects,all()
    serializer_class = AuthorSerializer
    permission_classes = (IsOwnerPermissions,)

#BookCategory Model CRUD-----------------------------------------------------------------------------
class ListCreatCategoryView(generics.ListCreateAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = (IsAuthenticated,)

class DetailUpdateDeleteCategoryView(generics.RetrieveUpdateDestroyAPIView):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer
    permission_classes = (IsOwnerPermissions,)