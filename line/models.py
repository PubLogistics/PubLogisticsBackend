from django.db import models
from company.models import Company

# Create your models here.
class Line(models.Model):
    id=models.IntegerField(primary_key=True,verbose_name="线路列表编号")
    name=models.CharField(max_length=32,verbose_name="线路名称")
    company=models.ForeignKey(Company,on_delete=models.CASCADE,related_name="line_in_company",verbose_name="运营公司")
    abbreviation=models.CharField(max_length=50,blank=True,verbose_name="线路简称")
