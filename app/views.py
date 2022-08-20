import json
from django.shortcuts import redirect, render, HttpResponse ,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login
import requests , base64,re ,os
# Create your views here.

#实现用户的登录
all_user=['root']
all_passwd={'root':'kali'}
def write (request,context=None):
    return render(request,'write.html',context)
def login(request):
    #网页的title
    #如果method是 post验证用户名 和 密码 是否正确
    if request.method =="POST":
        #获取用户名和密码
        user=request.POST.get('user')
        passwd= request.POST.get('passwd')
        #如果用户名和密码正确，跳转到write.html 让用户进行书写
        if user in all_user and passwd ==all_passwd[user] :
            context={'title':'write','user':user ,'say_hello':'hello'}
            #尝试了很久，哈哈哈，就是瞎jb试，查了一下，重定向，直接使用redirect没办法传递参数可以采用cookie 或session然后另一个视图尝试读取
            return  write( request,context)
        #如果用户名正确,密码错误，提示密码错误
        elif user in all_user and passwd !=all_passwd[user] :
            context={'title':'登录','user':user,'say_hello':'sorry your password is wrong'}
            return   render(request ,'login.html',context )
        else: 
            #如果登录用户名不存在
            context={'title':'登录','user':'none','say_hello':'sorry your username not found'}
            return render(request,'login.html',context)
    else:
        #如果method不是post，给用户显示登录界面
        context={'title':'登录','user':'游客','say_hello':'请登录'}
        return render(request,'login.html',context)
#在这里些一个注册页面
def register(request):
    #添加用户
    if request.method=="POST" :
        #获取注册的用户名和密码
        user=request.POST.get('user')
        passwd= request.POST.get('passwd')
        if user in all_user :
            return  render(request,"main.html",)
        else:
            all_user.append(user)
            all_passwd[user]=passwd
            return render(request,"login.html")
    else :
        return render(request,"register.html")
def main(request):
    return render (request,"main.html")

def get_vpn(request):
    url = 'https://s1.subbitznet.com/api/v1/client/subscribe?token=b7546ca2e57afc3803e4fbc76e12f999'
    response= requests.get(url)
    html=response.text
    text=base64.b64decode(html).decode('utf-8')
    ips=re.findall('\w\w\w\w\d.bitznet.cloud:\d\d\d\d\d',text)
    vpn_list=[]
    for ip  in ips :
        ip_port=ip.split(':')
        list="-s {} -p {} -l 1080 -k eccd5eba-0460-415e-b1cf-7cf6f96d4e51 -b 127.0.0.1 -l 1080 -m cert.bitbyte.one".format(ip_port[0],ip_port[1])
        vpn_list.append(list)
        context={'title':'vpn','vpn_list':vpn_list,'text':text}
    return render(request,'response.html',context)







    

    




    

