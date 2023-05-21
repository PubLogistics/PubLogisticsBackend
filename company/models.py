from django.db import models

# Create your models here.
class Company(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="运营公司编号")
    name=models.CharField(max_length=255,verbose_name="运营公司名称")
    abbreviation=models.CharField(max_length=50,blank=True,verbose_name="运营公司简称")
