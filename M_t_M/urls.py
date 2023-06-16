from django.urls import path, include
from M_t_M.views import *

urlpatterns = [
    path('', home, name="home"),
    path('about-us', AboutUs, name="AboutUs"),

    path('add-customer', add_customer, name="add_customer"),
    path('edit-customer', edit_customer, name="edit_customer"),

    path('add-product', add_product, name="add_product"),
    # path('edit-product', edit_product, name="edit_product"),
    path('edit-product/', EditProductView.as_view(), name='edit_product'),
    
    path('display-customer', display_customer, name="display_customer"),
    path('display-product', display_product, name="display_product"),
]
