import demjson
from django.contrib.auth.models import User
from django.db.models import QuerySet
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from django.contrib import auth
from django.core import serializers

from .models import Company

from .forms import CompanyCreateForm

from .method import model2jsonArr

# Create your views here.
class CompanyOperation(View):
    #CP01 运营公司信息创建
    def post(self,request)->JsonResponse:
        body=demjson.decode(request.body)
        company_form=CompanyCreateForm(body)
        if not company_form.is_valid():
            return JsonResponse({"msg":"请求不符合规范"},status=400)
        company=company_form.save()
        return JsonResponse({"msg":"创建公司成功","id":company.id},status=201)
    #CP02 运营公司信息查询
    def get(self,request)->JsonResponse:
        id=request.GET.get('id')
        name_like=request.GET.get('name',default="")
        abb_like=request.GET.get("abbreviation",default="")
        if id:
            company_query= Company.objects.raw("SELECT * FROM company_company WHERE id=%s",[id])
        else:
            name_like="%"+name_like+"%"
            abb_like="%"+abb_like+"%"
            company_query= Company.objects.raw("SELECT * FROM company_company WHERE name LIKE %s AND abbreviation LIKE %s ",[name_like,abb_like])
            print(type(company_query))
        # print(company_query)
        # company_query=list(company_query)
        # company_list=serializers.serialize('json',company_query)
        # company_list=company_list["field"]
        # company_list=company_query.values()
        company_list=model2jsonArr(company_query)
        print(company_list)
        return JsonResponse({"companys":company_list},status=200)
