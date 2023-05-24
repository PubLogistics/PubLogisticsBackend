import demjson
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.views import View
from django.contrib import auth

from .models import UserInfo

from .forms import RegisterForm,UserForm



class UserOperation(View):
    #US0101 用户注册
    def post(self,request)->JsonResponse:
        body=demjson.decode(request.body)
        # if User.objects.filter(username=body["username"]).exists():
        #     return JsonResponse({"msg":"用户名已经被占用，请更换用户名"},status=409)
        user_form=UserForm(body)
        user_info_form=RegisterForm(body)
        if not user_form.is_valid():
            return JsonResponse({"msg":user_form.errors},status=400)
        if not user_info_form.is_valid():
            return JsonResponse({"msg":user_info_form.errors},status=400)
        user=user_form.save(commit=False)#使用commit=False可以提供一个模型对象，以便于进行进一步的设置
        user.set_password(user_form.cleaned_data["password"])
        user.save()
        user_info=user_info_form.save(commit=False)
        user_info.user=user
        user_info.save()
        #需要加入校验验证码的步骤
        #可能需要另外存储password不能直接通过表单存储，还需要看看
        #不知道如果是继承的话，是不是可以直接通过表单保存
        #如果使用的是onetoonefield可能不大行直接通过forms内的password保存？
        return JsonResponse({"msg":"注册成功","id":user.id},status=201)
    
    #US0201 用户登录
    def get(self,request)->JsonResponse:
        body=demjson.decode(request.body)
        # user_form=UserForm(body)
        if not User.objects.filter(username=body["username"]).exists():
            return JsonResponse({"msg":"用户不存在"},status=400)
        # if not user_form.is_valid():
        #     return JsonResponse({"msg":user_form.errors},status=400)
        user=auth.authenticate(username=body["username"],password=body["password"])
        if not user.is_active:
            return JsonResponse({"msg":"用户名或者密码错误！"},status=403)
        auth.login(request,user)
        return JsonResponse({"msg":"登录成功"},status=200)
