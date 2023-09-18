from django.urls import path
from .views import MenuListView
from .views import MenuCreateView

urlpatterns = [
     path('menu/', MenuListView.as_view(), name='menu_list'),
     path('menu/create/', MenuCreateView.as_view(), name='menu_create'),
]