from django.db import models
from django.contrib.auth.models import User
# from django.db.models.signals import post_save
# from django.dispatch import receiver
from company.models import Company

# Create your models here.
class UserInfo(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        primary_key=True,
        verbose_name="用户",
    )
    nickname=models.CharField(max_length=64,verbose_name="用户昵称")
    conductor=models.BooleanField(default=False,verbose_name="司乘权限")
    company=models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True,verbose_name="所在公司")
    wage=models.DecimalField(default=0.0,max_digits=6,decimal_places=2,blank=True,verbose_name="钱")

# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         UserInfo.objects.create(user=instance)


# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()