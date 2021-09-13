
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_page'),
    path('about/', views.about, name='about_page'),
    path('all_wishes/', views.all_wish_list, name='wish_list_all'),
    path('wisher/<int:pk>/', views.list_page, name='wish_list_page'),
]
