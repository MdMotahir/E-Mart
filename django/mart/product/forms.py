from django import forms
from product.models import *

class ProductAddForm(forms.ModelForm):
    class Meta:
        model=Product
        fields=('name','category','unite_price','front_image','back_image','right_image','left_image','stock','discount','description','information')


        