from django.shortcuts import render
from product.models import *
# Create your views here.
from django.views import generic,View

class ProductListView(generic.ListView):
    model=Product
    template_name='product/Home.html'
    queryset=Product.objects.all()
    context_object_name='products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category=Category.objects.all()
        context["category"] = category 
        return context