from django.urls import path,include
from product.views import *

urlpatterns = [
    path('',ProductListView.as_view(),name='Home'),
]
