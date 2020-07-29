from django.urls import path

from . import views

app_name = "shop_cart"

urlpatterns = [
    #url for the Product list
    path('',views.product_list,name="product_list"),
    #url for the Product list by category
    path('<slug:category_slug>/',views.product_list,name='product_list_by_category'),
    #url for the product details
    path('<int:id>/<slug:slug>/',views.product_detail,name='product_detail'),
]