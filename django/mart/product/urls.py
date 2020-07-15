from django.urls import path,include
from product.views import *


urlpatterns = [
    path("",ProductListView.as_view(),name="Home"),

    path("Shop",ShopingListView.as_view(),name="Shop"),

    path("search",Search.as_view(),name='search'),

    path('my_cart',My_Cart.as_view(),name='cart'),

    path('checkout',checkout.as_view(),name='checkout'),

    path('my_order',OrderView.as_view(),name='my_order'),

    path('Product/<slug:slug>',ProductDetailsView.as_view(),name='Product Details'),

    path('add',ProductAddView.as_view(),name="add product"),

    path('add_cart/<slug:slug>',AddToCart.as_view(),name='add_cart'),

    path('add_cart_details/<slug:slug>',AddToCartDetails.as_view(),name='AddToCartDetails'),

    path('order/<slug:slug>',OrderNow.as_view(),name='order'),

    path('order_details/<int:id>',OrderDetails.as_view(),name='Details'),

    path('Product/<slug:slug>/update',ProductUpdateView.as_view()),

    path('Review/<slug:slug>',ReviewPart.as_view(),name='Review'),
]
