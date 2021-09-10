
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index_page'),
    path('about/', views.about, name='about_page'),
    path('wisher/<int:pk>/', views.list_page, name='wish_list_page'),
]
