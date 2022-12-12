import random
import re

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django_redis import get_redis_connection

# Create your views here.
from django.urls import reverse
from django.views import View

from app01.models import Userinfo
from utils.tencent.sms import send_sms_single,send_sms_multi


def sms(request):
    # login-->1618505 register-->1618507 reset_pass-->1618502
    result = send_sms_single("18030457381", 1618507, [666, ])
    print(result)
    return HttpResponse('ok')

def sms_xzdd(request):
    # login-->1618505 register-->1618507 reset_pass-->1618502 3v1-->1619426
    result = send_sms_multi(["18030457381","17345765787","18980566630","18880412935","18221273545"], 1619426, ["三Vs一", ])
    print(result)
    return HttpResponse('ok')

class IndexView(View):
    def get(self,request):
        return render(request,'index.html')

class SmsView(View):
    def post(self,request):
        mobile_phone = request.POST.get('mobile_phone')
        # 验证手机号 /^1[3-9]\d{9}$/
        if not re.match(r'^1[3-9]\d{9}$',mobile_phone):
            return JsonResponse(({'res': 2,'message': '手机号格式不正确'}))

        # 生成验证码，并存放redis
        verification_code =''.join(str(i) for i in random.sample(range(0, 9), 6))
        conn = get_redis_connection('default')
        conn.set(mobile_phone,verification_code,ex=300)

        template_id = 1618507
        send_sms_single(mobile_phone,template_id,[verification_code,])
        return JsonResponse(({'res': 1,'message': '验证码发送成功'}))

class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')

    def post(self,request):
        '''用户注册'''
        # 获取前端提交数据
        username = request.POST.get('username')
        password = request.POST.get('password')
        valid_password = request.POST.get('valid_password')
        mobile_phone = request.POST.get('mobile_phone')
        verification_code = request.POST.get('verification_code')

        # todo username pasword valid_password mobile_phone 输入空格或TAB判断


        # 验证前端提交数据完整性
        if not all([username,password,valid_password,mobile_phone,verification_code]):
            return render(request,'register.html',{'errmsg':'数据不完整，请检查输入信息'})

        if password!=valid_password:
            return render(request,'register.html',{'errmsg':'两次密码不一致'})

        #^(?![0-9]+$)(?![a-zA-Z_]+$)[0-9A-Za-z_]{8,16}$ 密码长度为8-16位，需包含数字和字母(大小写均可)
        if not re.match(r'^(?![0-9]+$)(?![a-zA-Z_]+$)[0-9A-Za-z_]{8,16}$',password):
            return render(request,'register.html',{'errmsg':'密码长度为8-16位，需包含数字和字母(大小写均可)'})

        # 验证手机号 /^1[3-9]\d{9}$/
        if not re.match(r'^1[3-9]\d{9}$',mobile_phone):
            return render(request, 'register.html', {'errmsg': '手机号格式不正确'})

        #验证用户是否存在
        # if Userinfo.objects.get(username=username):
        #     return render(request, 'register.html', {'errmsg': '用户已存在'})

        try:
            user = Userinfo.objects.get(username=username)
        except Userinfo.DoesNotExist:
            user = None
        if user:
            return render(request, 'register.html', {'errmsg': '用户名已存在'})

        #验证验证码是否正确
        conn = get_redis_connection('default')
        verification_code_redis = conn.get(mobile_phone)
        if verification_code != verification_code_redis.decode('utf-8'):
            return render(request, 'register.html', {'errmsg': '验证码错误'})

        Userinfo.objects.create(username=username, password=password,mobile_phone=mobile_phone)

        return redirect(reverse('app01:index'))

