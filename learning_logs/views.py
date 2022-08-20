from tkinter.messagebox import NO
from django.shortcuts import render ,HttpResponse   #处理--响应
from .models   import  Topic ,Blogs 

# Create your views here.
#创建所有笔记的索引
def note(request):
    blog=['HELLO','HI','NIHAO']
    context={'title':'笔记集合'}
    return render(request,'note.html',context)
#网络相关知识的笔记
def network(request):
    if request.method == "POST":
        #保存主题
        titles=[topic.title  for topic in Topic]
        r=Topic(title=request.POST.get('title'))
        if r not in titles:
            r.save()
        blog=Blogs(title=r,text=request.POST.get('text'))
        blog.save()
        blogs=Blogs.objects.all()
        context={'title':'networK','blogs':blogs}
        return render(request,'network.html',context)
    else:
        blogs=Blogs.objects.all()
        context={'title':'network','blog':blogs}
        return render(request,'network.html',context)

# 增加主题
def add_topic(request):
    pass
def add_text(request):  
    pass 
#展示Blogs内容
def show_blog(request):
    pass
















