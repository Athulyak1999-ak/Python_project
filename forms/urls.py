
from django.urls import path
from . import views

urlpatterns = [
            path("list", views.listbook, name='lists'),
            path('create/', views.createBook, name='create'),
            path("author/", views.createAuthor, name='author'),
            path('updates/<int:book_id>/', views.updateView, name='update'),
            path('details/<int:book_id>/', views.detailsView, name='details'),

            path('deletes/<int:book_id>/', views.deleteView, name='delete'),
            path('index/', views.index),
            path('search/', views.searchBook, name='search'),



]