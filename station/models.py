from django.db import models
from line.models import Line

# Create your models here.
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
