from django.db import models
from user.models import UserInfo
from line.models import Line

# Create your models here.
class Vehicle(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="交通工具编号")
    line=models.ManyToManyField(Line,blank=True,related_name="line",verbose_name="所运行在的线路")

class VehicleConduct(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="司乘列表编号")
    conductor=models.ManyToManyField(UserInfo,related_name="vehicle_conductor",verbose_name="司乘人员")
    start_time=models.DateTimeField(verbose_name="司乘开始时间")
    end_time=models.DateTimeField(verbose_name="司乘结束时间")
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE,related_name="conducting_vehicle",verbose_name="司乘交通工具")
    line=models.ForeignKey(Line,blank=True,on_delete=models.CASCADE,related_name="conducting_line",verbose_name="司乘线路")
