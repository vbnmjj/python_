from django.urls import path
from . import views

urlpatterns = [
      path('network/',views.network,name='network'),
      path('',views.note),
]
