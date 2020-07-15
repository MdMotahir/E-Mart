from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.
from django.contrib.auth.admin import UserAdmin


admin.site.register(get_user_model(),UserAdmin)