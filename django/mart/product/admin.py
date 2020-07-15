from django.contrib import admin
from product.models import *
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

class ProductAdmin(SummernoteModelAdmin):
    summernote_field=('description','information',)


admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Items)
admin.site.register(Cart)
admin.site.register(Order)
admin.site.register(Review)