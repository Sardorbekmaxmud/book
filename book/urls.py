from django.urls import path
from .views import (ListCreateBookView,DetailUpdateDeleteBookView,
                    ListCreatAuthorView,DetailUpdateDeleteAuthorView,
                    ListCreatCategoryView,DetailUpdateDeleteCategoryView)

urlpatterns = [
# book URL------------------------------------------------------------------------------
    path('book/',ListCreateBookView.as_view()),
    path('book/<pk>/',DetailUpdateDeleteBookView.as_view()),
# author URL----------------------------------------------------------------------------
    path('author/',ListCreatAuthorView.as_view()),
    path('author/<pk>/',DetailUpdateDeleteAuthorView.as_view()),
#category URL---------------------------------------------------------------------------
    path('category/',ListCreatCategoryView.as_view()),
    path('category/<pk>/',DetailUpdateDeleteCategoryView.as_view()),
]