from django.db.models.signals import post_save,pre_save
from django.dispatch import receiver
from product.models import *

# @receiver(post_save,sender=Order)
# def Stock_calculate(sender,instance,created,**kwargs):
#     print(instance.orderitems.all())
#     l1=sender.objects.filter(user=instance.user)

#     for i in l1\:
#         print(i.name)
#     if created:
#         for i in instance.orderitems.all():
#             pritn("one")
#         print("Hy")
#     else:
#         print('Bye')