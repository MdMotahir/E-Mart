from django.shortcuts import render
from product.models import *
# Create your views here.
from django.views import generic,View
from product.forms import *

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


class ProductDetailsView(generic.DetailView):
    model=Product
    template_name="product/Product Details.html"

class ProductAddView(generic.CreateView):
    model=Product
    form_class=ProductAddForm
    template_name='product/ProductAdd.html'
    success_url='/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)
