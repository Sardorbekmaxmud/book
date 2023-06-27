from django.shortcuts import render,get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import BookModel,AuthorModel,BookCategory
from .serializer import BookSerializer,AuthorSerializer,BookCategorySerializer

# Create your views here.
class AllBookApiView(APIView):
    def get(self,request,*args,**kwargs):
        all_book = BookModel.objects.all()
        serializer = BookSerializer(all_book,many=True)
        return Response(serializer.data)

class DetailBookApiView(APIView):
    def get(self,request,*args,**kwargs):
        book = get_object_or_404(BookModel,pk=kwargs['book_id'])
        serializer = BookSerializer(book)
        return Response(serializer.data)

class CreateBookApiView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

class UpdateBookApiView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(BookModel,pk=kwargs['book_id'])
        serializer = BookSerializer(instance,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteBookApiView(APIView):
    def delete(self,request,*args,**kwargs):
        book = get_object_or_404(BookModel,pk=kwargs['book_id'])
        book.delete()
        return Response({"message":"status"},status=status.HTTP_204_NO_CONTENT)

# AuthorModel CRUD ---------------------------------------------
class AllAuthorApiView(APIView):
    def get(self,request,*args,**kwargs):
        authors = AuthorModel.objects.all()
        serializer = AuthorSerializer(authors,many=True)
        return Response(serializer.data)

class DetailAuthorApiView(APIView):
    def get(self,request,*args,**kwargs):
        author = get_object_or_404(AuthorModel,pk=kwargs['author_id'])
        serializer = AuthorSerializer(author)
        return Response(serializer.data)

class CreateAuthorApiView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = AuthorSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateAuthorApiView(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(AuthorModel,pk=kwargs["author_id"])
        serializer = AuthorSerializer(instance,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteAuthorApiView(APIView):
    def delete(self,request,*args,**kwargs):
        author = get_object_or_404(AuthorModel,pk=kwargs['author_id'])
        author.delete()
        return Response({"message":"successfully deleted"},status=status.HTTP_204_NO_CONTENT)

#BookCategory Model CRUD-----------------------------------------------------------------------------
class AllCategoryApiView(APIView):
    def get(self,request,*args,**kwargs):
        all_category = BookCategory.objects.all()
        serializer = BookCategorySerializer(all_category,many=True)
        return Response(serializer.data)

class DetailCategoryApiView(APIView):
    def get(self,request,*args,**kwargs):
        category = get_object_or_404(BookCategory,pk=kwargs['category_id'])
        serializer = BookCategorySerializer(category)
        return Response(serializer.data)

class CreateCategoryApiView(APIView):
    def post(self,request,*args,**kwargs):
        serializer = BookCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class UpdateCategoryApiVIew(APIView):
    def patch(self,request,*args,**kwargs):
        instance = get_object_or_404(BookCategory,pk=kwargs['category_id'])
        serializer = BookCategorySerializer(instance,request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class DeleteCategoryApiView(APIView):
    def delete(self,request,*args,**kwargs):
        category = get_object_or_404(BookCategory,pk=kwargs['category_id'])
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)