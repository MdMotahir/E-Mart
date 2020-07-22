from django import forms
from product.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ProductAddForm(forms.ModelForm):
    description=forms.CharField(widget=SummernoteWidget())
    information=forms.CharField(widget=SummernoteWidget())
    featured=forms.BooleanField()
    class Meta:
        model=Product
        fields=('name','category','unite_price','front_image','back_image','right_image','left_image','featured','stock','description','information')


class AddCartForm(forms.Form):
    quantity=forms.IntegerField()

class ReviewForm(forms.ModelForm):
    rating_range=[(1,1),(2,2),(3,3),(4,4),(5,5)]
    rating=forms.ChoiceField(choices=[rating_range], required=True)
    class Meta:
        model = Review 
        fields = ('comment','rating',)