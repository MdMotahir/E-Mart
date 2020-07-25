from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    email=models.EmailField(unique=True)
    contact=models.CharField(max_length=10)
    address1=models.TextField()
    address2=models.TextField()
    postal_code=models.IntegerField()
    is_seller=models.BooleanField(default=False)

    REQUIRED_FIELDS=('email','contact','address1','first_name','last_name','postal_code','is_seller',)

    def __str__(self):
        return self.username