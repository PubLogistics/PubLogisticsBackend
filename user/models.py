import mailbox
from django.db import models
from django.contrib.auth.models import User
from route.models import Company

# Create your models here.
class UserProfile(models.Model):
    user=models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name="profile",
        primary_key=True,
        verbose_name="用户",
    )
    nickname=models.CharField(max_length=64,verbose_name="用户昵称")
    conductor=models.BooleanField(default=False,verbose_name="司乘权限")
    company=models.ForeignKey(Company,on_delete=models.SET_NULL,blank=True,verbose_name="所在公司")
    wage=models.DecimalField(default=0.0,max_digits=None,decimal_places=2,blank=True,verbose_name="钱")

