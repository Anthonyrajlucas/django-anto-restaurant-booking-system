from django.shortcuts import render
from .models import MenuItem
from .forms import MenuItemForm
from django.views.generic import ListView, CreateView

class MenuListView(ListView):
    model = MenuItem
    template_name = 'menu_list.html'
    context_object_name = 'menu_items'

class MenuCreateView(CreateView):
    model = MenuItem
    form_class = MenuItemForm
    template_name = 'menu_form.html'