from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group

@receiver(post_save,sender=get_user_model())
def assign_default_group(sender,instance,created,**kwargs):
    if created:
        Buyer=Group.objects.get(name='Buyer')
        Seller=Group.objects.get(name='Seller')
        if instance.is_seller == False:
            instance.groups.add(Buyer)
        else:
            instance.groups.add(Seller)