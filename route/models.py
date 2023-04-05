from django.db import models
from express.models import Package
from user.models import UserProfile

# Create your models here.
class Company(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="运营公司编号")
    name=models.CharField(max_length=255,verbose_name="运营公司名称")
    abbreviation=models.CharField(max_length=50,blank=True,verbose_name="运营公司简称")

class Line(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="线路列表编号")
    name=models.CharField(max_length=32,verbose_name="线路名称")
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name="line_in_company",verbose_name="运营公司")
    abbreviation=models.CharField(max_length=50,blank=True,verbose_name="线路简称")

class StationName(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="车站名列表编号")
    name=models.CharField(max_length=64,verbose_name="车站名")
    line=models.ForeignKey(Line,on_delete=models.CASCADE,related_name="station_on_line",verbose_name="所属线路")
    id_in_line=models.CharField(max_length=5,blank=True,verbose_name="线内编号")

class Station(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="车站编号")
    direction=models.CharField(blank=True,max_length=32,verbose_name="行驶方向")
    location=models.CharField(blank=True,max_length=255,verbose_name="车站位置")
    name=models.ManyToManyField(StationName,related_name="station_name",verbose_name="车站名称")

class DeliverAddress(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="地址编号")
    location=models.CharField(max_length=255,verbose_name="地址位置")
    raiser=models.ForeignKey(UserProfile,on_delete=models.CASCADE,related_name="address_raiser",verbose_name="地址创建人")

class Vehicle(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="交通工具编号")
    line=models.ManyToManyField(Line,blank=True,related_name="line",verbose_name="所运行在的线路")

class VehicleConduct(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="司乘列表编号")
    conductor=models.ManyToManyField(UserProfile,related_name="vehicle_conductor",verbose_name="司乘人员")
    start_time=models.DateTimeField(verbose_name="司乘开始时间")
    end_time=models.DateTimeField(verbose_name="司乘结束时间")
    vehicle=models.ForeignKey(Vehicle,on_delete=models.CASCADE,related_name="conducting_vehicle",verbose_name="司乘交通工具")
    line=models.ForeignKey(Line,blank=True,on_delete=models.CASCADE,related_name="conducting_line",verbose_name="司乘线路")

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