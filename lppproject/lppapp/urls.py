from . import views
from django.urls import path
from lppproject import settings

urlpatterns = [
    path('', views.demo, name='demo'),
    # path('opp/', views.operations, name='operations'),
]
