from django.urls import path
from .views import (AllBookApiView,DetailBookApiView,CreateBookApiView,UpdateBookApiView,DeleteBookApiView,
                    AllAuthorApiView,DetailAuthorApiView,CreateAuthorApiView,UpdateAuthorApiView,DeleteAuthorApiView,
                    AllCategoryApiView,DetailCategoryApiView,CreateCategoryApiView,UpdateCategoryApiVIew,DeleteCategoryApiView)

urlpatterns = [
# book URL------------------------------------------------------------------------------
    path('book/',AllBookApiView.as_view()),
    path('book/<int:book_id>/',DetailBookApiView.as_view()),
    path('book/create/',CreateBookApiView.as_view()),
    path('book/update/<int:book_id>/',UpdateBookApiView.as_view()),
    path('book/delete/<int:book_id>/',DeleteBookApiView.as_view()),
# author URL----------------------------------------------------------------------------
    path('author/',AllAuthorApiView.as_view()),
    path('author/<int:author_id>/',DetailAuthorApiView.as_view()),
    path('author/create/',CreateAuthorApiView.as_view()),
    path('author/update/<int:author_id>/',UpdateAuthorApiView.as_view()),
    path('author/delete/<int:author_id>/',DeleteAuthorApiView.as_view()),
#category URL---------------------------------------------------------------------------
    path('category/',AllCategoryApiView.as_view()),
    path('category/<int:category_id>/',DetailCategoryApiView.as_view()),
    path('category/create/',CreateCategoryApiView.as_view()),
    path('category/update/<int:category_id>/',UpdateCategoryApiVIew.as_view()),
    path('category/delete/<int:category_id>/',DeleteCategoryApiView.as_view()),
]