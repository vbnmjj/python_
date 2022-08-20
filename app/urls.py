from django.urls import path
from app import views

urlpatterns = [
    # 将函数绑定至对应路由
    path('login/',views.login ,name='login') ,
    path('register/',views.register,name='register'),
    path('write/',views.write,name='write'),
    path('',views.main),
    path('response.html',views.get_vpn ,name="response")
]
