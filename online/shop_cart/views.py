from django.shortcuts import render, get_object_or_404

from .models import Category, Product

# Creating the catalog view
def product_list(request, category_slug=None):
    category = None

