from django import forms
from product.models import *
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget

class ProductAddForm(forms.ModelForm):
    description=forms.CharField(widget=SummernoteWidget())
    information=forms.CharField(widget=SummernoteWidget())
    class Meta:
        model=Product
        fields=('name','category','unite_price','front_image','back_image','right_image','left_image','stock','description','information')


class AddCartForm(forms.Form):
    quantity=forms.IntegerField()

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review 
        fields = ('comment','rating',)
        widgets = {'rating': forms.NumberInput(attrs={'class': 'Stars'})}
        labels = {'note': 'Note /5'}