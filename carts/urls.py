from django.urls import path
from . import views


app_name = 'carts'

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add_item/', views.add_item, name='add_item'),
    path('api/products/<int:product_id>/', views.product_info, name='product_info'),
    path('order_page/', views.order_page, name='order_page'),
    path('kakaopay/', views.kakaopay, name='kakaopay'),
    path('kakaopay/success/', views.kakaopay_success, name='kakaopay_success'),
    path('kakaopay/fail/', views.kakaopay_fail, name='kakaopay_fail'),
    path('kakaopay/cancel/', views.kakaopay_cancel, name='kakaopay_cancel'),
]