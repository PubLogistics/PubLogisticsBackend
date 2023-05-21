from django.db import models
from express.models import Package
from user.models import UserInfo
from line.models import Line
from station.models import Station
from vehicle.models import Vehicle

# Create your models here.

class DeliverAddress(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="地址编号")
    location=models.CharField(max_length=255,verbose_name="地址位置")
    raiser=models.ForeignKey(UserInfo,on_delete=models.CASCADE,related_name="address_raiser",verbose_name="地址创建人")


class Route(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="路径编号")
    from_type=models.BooleanField(default=False,verbose_name="起始点类型")
    to_type=models.BooleanField(default=False,verbose_name="到达点类型")
    step=models.IntegerField(default=0,verbose_name="步骤")
    start_time=models.DateTimeField(blank=True,verbose_name="路程开始时间")
    end_time=models.DateTimeField(blank=True,verbose_name="路程结束时间")
    package=models.ForeignKey(Package,on_delete=models.CASCADE)
    from_type_0=models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,related_name="from_station",verbose_name="站点起始点")
    to_type_0=models.ForeignKey(Station,on_delete=models.CASCADE,blank=True,related_name="to_station",verbose_name="站点结束点")
    from_type_1=models.ForeignKey(DeliverAddress,on_delete=models.CASCADE,blank=True,related_name="from_location",verbose_name="自定起始点")
    to_type_1=models.ForeignKey(DeliverAddress,on_delete=models.CASCADE,blank=True,related_name="to_location",verbose_name="自定结束点")
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE,related_name="vehicle_of_route",verbose_name="车辆信息")
    line=models.ForeignKey(Line,on_delete=models.CASCADE,blank=True,related_name="line_of_route",verbose_name="使用线路")