from django.db import models
from user.models import UserInfo

# Create your models here.
class Package(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="包裹编号")
    name=models.CharField(max_length=255,verbose_name="包裹名称")
    addresser=models.ForeignKey(UserInfo,on_delete=models.DO_NOTHING,related_name="addresser",verbose_name="发件人")
    addressee=models.ForeignKey(UserInfo,on_delete=models.DO_NOTHING,related_name="addressee",verbose_name="收件人")
    photo=models.URLField(blank=True,verbose_name="外观")
    large=models.BooleanField(default=False,verbose_name="大件")
    send_time=models.DateTimeField(blank=True,verbose_name="发货时间")
    receive_time=models.DateTimeField(blank=True,verbose_name="收货时间")



