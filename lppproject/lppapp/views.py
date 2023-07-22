from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Person
# Create your views here.
def demo(request):
    obj=Place.objects.all()
    hm=Person.objects.all()
    return render(request,"hom.html",{'result':obj,'res':hm})
# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#     sub=x-y
#     mul=x*y
#     div=x/y
#     return render(request,"result.html",{'result':res,'subs':sub,'mult':mul,'divs':div})
#
#
