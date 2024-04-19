from django.urls import path
from . import views

urlpatterns = [
    path('user_bookList/', views.userListBook, name='user_lists'),
    path('user_bookDetails/<int:book_id>/', views.UserBookDetails, name='user_details'),
    path('user_search/', views.User_searchBook, name='userSearch'),
    path('add_to_cart/<int:book_id>/', views.add_to_cart, name='AddToCart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('increase/<int:item_id>/', views.increase_quantity, name='increase_quantity'),
    path('decrease/<int:item_id>/', views.decrease_quantity, name='decrease_quantity'),
    path('remove_from_cart/<int:item_id>/', views.remove_from_cart, name='remove_cart'),
    path('create_checkout_session/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
    path('cancel/', views.cancel, name='cancel')

]