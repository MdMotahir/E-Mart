from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
# Create your models here.

class Category(models.Model):
    name=models.CharField(max_length=50)
    image=models.ImageField(upload_to='category/',blank=True)
    description=models.TextField()
    slug=models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)

class Product(models.Model):
    name=models.CharField(max_length=150)
    description=models.TextField()
    information=models.TextField()
    unite_price=models.DecimalField(max_digits=8, decimal_places=2)
    front_image=models.ImageField(upload_to='product/')
    back_image=models.ImageField(upload_to='product/')
    right_image=models.ImageField(upload_to='product/')
    left_image=models.ImageField(upload_to='product/')
    stock=models.IntegerField()
    discount=models.FloatField(blank=True)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.SlugField(blank=True)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)


class Cart(models.Model):
    user=models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    item=models.ForeignKey(Product,on_delete=models.CASCADE)
    quantity=models.IntegerField(default=1)
    total=models.DecimalField(max_digits=8, decimal_places=2,blank=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.quantity} of {self.item.name}'

    def save(self,*args,**kwargs):
        self.total = self.item.unite_price * self.quantity
        super().save(*args,**kwargs)


class Order(models.Model):
    orderitems=models.ManyToManyField(Cart)
    user=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_order=models.BooleanField(default=False)
    order_date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    
    def get_total_price(self):
        total=0
        for i in self.orderitems.all():
            total+=i.total
        return total