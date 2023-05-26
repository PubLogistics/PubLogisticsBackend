import demjson
from django.contrib.auth.models import User
from django.db import connection
from django.db.models import QuerySet
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.utils.decorators import method_decorator

from .models import Company

from .forms import CompanyCreateForm,CompanyModifyForm

from .method import model2jsonArr

# Create your views here.
class CompanyOperation(View):
    #CP01 运营公司信息创建
    @method_decorator(login_required)
    def post(self,request)->JsonResponse:
        body=demjson.decode(request.body)
        company_form=CompanyCreateForm(body)
        if not company_form.is_valid():
            return JsonResponse({"msg":"请求不符合规范"},status=400)
        company=company_form.save()
        return JsonResponse({"msg":"创建公司成功","id":company.id},status=201)
    #CP02 运营公司信息模糊查询
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
            # print(type(company_query))
        # print(company_query)
        # company_query=list(company_query)
        # company_list=serializers.serialize('json',company_query)
        # company_list=company_list["field"]
        # company_list=company_query.values()
        company_list=model2jsonArr(company_query)
        # print(company_list)
        return JsonResponse({"companys":company_list},status=200)
class CompanyIdOperation(View):
    #CP03 运营公司信息修改
    @method_decorator(login_required)
    def put(self,request,id:int)->JsonResponse:
        if not id:
            return JsonResponse({"msg":"没有传id参数"},status=400)
        body=demjson.decode(request.body)
        company_form=CompanyModifyForm(body)
        if not company_form.is_valid():
            return JsonResponse({"msg":"请求格式不符合要求"},status=400)
        find_result= Company.objects.raw("SELECT * FROM company_company WHERE id=%s",[id])
        company_list=model2jsonArr(find_result)
        if not company_list:
            return JsonResponse({"msg":"找不到需要修改的公司"},status=404)
        print(body)
        if 'name' in body:
            name=body['name']
            with connection.cursor() as cur:
                cur.execute("UPDATE company_company SET name=%s WHERE id=%s",[name,id])
        if 'abbreviation' in body:
            abb=body['abbreviation']
            with connection.cursor() as cur:
                cur.execute("UPDATE company_company SET abbreviation=%s WHERE id=%s",[abb,id])
        new_company_query=Company.objects.raw("SELECT * FROM company_company WHERE id=%s",[id])
        new_company_list=model2jsonArr(new_company_query)
        new_company_info=new_company_list[0]
        return JsonResponse({"company":new_company_info},status=200)
    @method_decorator(login_required)
    def delete(self,request,id:int)->JsonResponse:
        if not id:
            return JsonResponse({"msg":"没有传id参数"},status=400)
        find_result= Company.objects.raw("SELECT * FROM company_company WHERE id=%s",[id])
        company_list=model2jsonArr(find_result)
        if not company_list:
            return JsonResponse({"msg":"找不到需要删除的公司"},status=404)
        with connection.cursor() as cur:
                cur.execute("DELETE FROM company_company WHERE id=%s",[id])
        return JsonResponse({"msg":"删除成功！"},status=200)
        
        




        
        

