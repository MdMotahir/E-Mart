from django.urls import path,include
from product.views import *

urlpatterns = [
    path('',ProductListView.as_view(),name='Home'),

    path('Product/<slug:slug>',ProductDetailsView.as_view(),name='Product Details'),

    path('add',ProductAddView.as_view())
]
