from django.shortcuts import render, redirect
from product.models import *
# Create your views here.
from django.views import generic,View
from django.views.generic.edit import FormMixin,FormView
from product.forms import *
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.urls import reverse,reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin,UserPassesTestMixin
from django.db.models import Q
from django.core.paginator import Paginator
from django.db.models import Avg

class ContactUs(FormView):
    form_class=ContactUsForm
    success_url=reverse_lazy("Home")
    template_name="product/Contact Us.html"

class Search(View):
    def get(self,request):
        query=request.GET['query']
        products=Product.objects.filter(
                Q(name__icontains=query),
                Q(description__icontains=query),
                Q(information__icontains=query),
            ).distinct()
        context={'products':products,'query':query}
        return render(request,'product/Search.html',context)

class ProductListView(generic.ListView):
    model=Product
    template_name='product/Home.html'
    queryset=Product.objects.filter(featured=True)
    context_object_name='products'
    paginate_by=8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category=Category.objects.all()
        context["category"] = category 
        return context

class CategoryListView(View):
    def get(self,request,slug):
        category=Category.objects.all()
        cat=Category.objects.get(slug=slug)
        products=Product.objects.filter(featured=True)
        product=products.filter(category=cat)
        return render(request,"product/Fcategory.html",context={"cat":cat,"product":product,"category":category})
    
class ShopingListView(generic.ListView):
    model=Product
    template_name='product/Shoping.html'
    queryset=Product.objects.all()
    context_object_name='products'
    paginate_by=8

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category=Category.objects.all()
        context["category"] = category 
        return context

class ShopCategoryListView(View):
    def get(self,request,slug):
        category=Category.objects.all()
        cat=Category.objects.get(slug=slug)
        product=Product.objects.filter(category=cat)
        return render(request,"product/Category.html",context={"cat":cat,"product":product,"category":category})

class ProductDetailsView(generic.DetailView):
    model=Product
    template_name="product/Product Details.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        item_name=kwargs['object']
        item=Product.objects.get(name=item_name)
        review=Review.objects.filter(item=item)
        avg_rating=Review.objects.aggregate(Avg('rating'))
        context["review"] = review
        context["avg_rating"] = avg_rating
        return context

class ProductAddView(generic.CreateView):
    model=Product
    form_class=ProductAddForm
    template_name='product/ProductAdd.html'
    success_url='/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ProductUpdateView(generic.UpdateView):
    model=Product
    form_class=ProductAddForm
    template_name='product/Product Update.html'
    success_url='/'

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

class ReviewPart(LoginRequiredMixin,View):
    def get(self,request,slug):
        item_name=slug
        rating=request.GET['rating']
        comment=request.GET['comment']
        item=Product.objects.get(slug=item_name)

        review=Review.objects.create(
            item=item,
            user=request.user,
            comment=comment,
            rating=int(rating)
        )
        return redirect(reverse_lazy('Product Details', args=[slug]))

class AddToCartDetails(View):
    def get(self,request,slug):
        item_name=slug
        quantity_str=request.GET['quantity']
        quantity=int(quantity_str)
        if request.user.is_anonymous:
            cart=request.session.get('cart')
            if cart:
                if cart.get(item_name):
                    cart[item_name]=quantity
                else:
                    cart[item_name]=quantity
            else:
                cart={}
                cart[item_name]=quantity
            request.session['cart']=cart
            return redirect(reverse_lazy('Product Details', args=[slug]))
        else:
            item=Product.objects.get(slug=item_name)
            items=Items.objects.create(
                item=item,
                user=request.user
            )
            cart_items=Cart.objects.filter(user=request.user)
            if cart_items:
                cart=cart_items[0]
                product=cart.cartitems.filter(item__slug=item_name)
                if product:
                    product[0].quantity=quantity
                    product[0].save()
                    return redirect(reverse_lazy('Product Details', args=[slug]))
                else:
                    cart.cartitems.add(items)
                    items.quantity=quantity
                    items.save()
                    return redirect(reverse_lazy('Product Details', args=[slug]))
            else:
                cart=Cart.objects.create(user=request.user)
                cart.cartitems.add(items)
                items.quantity=quantity
                items.save()
                return redirect(reverse_lazy('Product Details', args=[slug]))


class AddToCart(View):
    def get(self,request,slug):
        item_name=slug
        if request.user.is_anonymous:
                cart=request.session.get('cart')
                if cart:
                    if cart.get(item_name):
                        cart[item_name]+=1
                    else:
                        cart[item_name]=1
                else:
                    cart={}
                    cart[item_name]=1
                request.session['cart']=cart
                return redirect(reverse_lazy('Home'))
        else:
            item=Product.objects.get(slug=slug)
            items=Items.objects.create(
                item=item,
                user=request.user
            )
            cart_items=Cart.objects.filter(user=request.user)
            if cart_items:
                cart=cart_items[0]
                product=cart.cartitems.filter(item__slug=item_name)
                if product:
                    product[0].quantity+=1
                    product[0].save()
                    return redirect(reverse('Home'))
                else:
                    cart.cartitems.add(items)
                    return redirect(reverse('Home'))
            else:
                cart,created=Cart.objects.get_or_create(user=request.user)
                cart.cartitems.add(items)
                return redirect(reverse('Home'))

class My_Cart(View):
    def get(self,request):
        if request.user.is_anonymous:
            if request.session.get('cart'):
                cart=request.session['cart']
                cart_items=[]
                for i,j in cart.items():
                    dic={}
                    item=Product.objects.get(slug=i)
                    dic[item]=j
                    cart_items.append(dic)
                total=0
                for dic in cart_items:
                    for i,j in dic.items():
                        total+=i.unite_price*j
                return render(request,"product/Cart Details.html",context={'total':total,'cart_items':cart_items})
            else:
                total=0
                cart_items=None
                return render(request,"product/Cart Details.html",context={'total':total,'items':cart_items})
        else:
            cart,created=Cart.objects.get_or_create(user=request.user)
            items=cart.cartitems.all()
            return render(request,"product/Cart Details.html",context={'cart':cart,'items':items})

class OrderNow(LoginRequiredMixin,View):
    def get(self,request,slug):
        item=Product.objects.get(slug=slug)
        items=Items.objects.create(
            item=item,
            user=request.user
        )
        order_list=Order.objects.create(user=request.user)
        order_list.orderitems.add(items)
        return redirect(reverse_lazy('Home'))

class checkout(LoginRequiredMixin,View):
    def get(self,request):
        cart=Cart.objects.get(user=request.user)
        cart_items=cart.cartitems.all()
        order=Order.objects.create(user=request.user)
        for i in cart_items.all():
            order.orderitems.add(i)
        cart.delete()
        return redirect(reverse_lazy('my_order'))

class OrderView(LoginRequiredMixin,View):
    def get(self,request):
        order=Order.objects.filter(user=request.user)
        return render(request,"product/Order Details.html",context={'order':order})

class OrderDetails(LoginRequiredMixin,View):
    def get(self,request,id):
        order=Order.objects.filter(id=id)
        order=order[0]
        items=order.orderitems.all()
        return render(request,"product/Order Detail Page.html",context={'order':order,'items':items})

class Wishlist(LoginRequiredMixin,View):
    def get(self,request,slug):
        item=Product.objects.get(slug=slug)
        items,created=Items.objects.get_or_create(
            user=request.user,
            item=item,
            )
        lists=MyWishlist.objects.filter(user=request.user)
        if lists:
            l1=lists[0]
            product=l1.items.filter(item__slug=slug)
            if product:
                product[0].quantity=1
                product[0].save()
                return redirect(reverse('Home'))
            else:
                l1.items.add(items)
                return redirect(reverse('Home'))
        else:
            lists,created=MyWishlist.objects.get_or_create(user=request.user)
            lists.items.add(items)
            return redirect(reverse('Home'))

class WishlistView(LoginRequiredMixin,View):
    def get(self,request):
        wishlist,created=MyWishlist.objects.get_or_create(user=request.user)
        items=wishlist.items.all()
        return render(request,"product/Wishlist.html",context={'wishlist':items})