# 在这里创建你的模型
from  django.db import models

#创建一个标题
class Topic (models.Model):
    title=models.CharField(max_length=150)
    def __str__(self):
        return self.title

#博文的主体内容
class Blogs(models.Model):
    #主题
    title=models.ForeignKey(Topic,on_delete=models.CASCADE)
    #正文
    text = models.TextField()
    #创建时间
    created_time = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.title ,self.text



