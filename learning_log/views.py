
# 这是一个处理 http 请求的模块 ，处理一个空网页
from django import views
from django.http import HttpResponse


# 直接对应一个模板内的网页进行回应  
from django.shortcuts import render 
def hello(request):
    return HttpResponse('这是一个空的网页，也是默认的页面')
def index(request):
    context={}
    context["name"]= "冯豪杰的程序"
    #列表
    views_list= ["hi","hello","你好"]
    context["views_list"]=views_list
    #字典
    views_dic={"name":'feng',"age":17}
    context["views_dic"]=views_dic
    #if/else 判断
    score=89
    context["score"]=score
    # 空列白
    empty_list=[]
    context["empty_list"]=empty_list

    return render(request,"index.html",context)  #返回给浏览器的一个网页  和 





