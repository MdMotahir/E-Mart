from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    slug=models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class Product(models.Model):
    name=models.CharField(max_length=150)
    desc=models.TextField()
    unite_price=models.DecimalField(max_digits=8, decimal_places=2)
    image=models.ImageField(upload_to=None,blank=True)
    stock=models.IntegerField()
    discount=models.FloatField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
    
class Item(models.Model):
    product=models.OneToOneField(Product,on_delete=models.CASCADE)
    quantity=models.PositiveIntegerField()
    price=models.DecimalField(max_digits=8, decimal_places=2,blank=True)

    def save(self,*args,**kwargs):
        self.price=self.product.unite_price*self.quantity
        super().save(*args,**kwargs)

class Cart(models.Model):
    user=models.OneToOneField(get_user_model(),on_delete=models.CASCADE)
    is_orderd=models.BooleanField()
    Item=models.ManyToManyField(Item)
    total_price=models.DecimalField(max_digits=8, decimal_places=2)

    
class Order(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    cart=models.OneToOneField(Cart,on_delete=models.CASCADE)
    date_created=models.DateTimeField(auto_now_add=True)