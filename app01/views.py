from django.shortcuts import render,HttpResponse,redirect
from app01.models import *
# Create your views here.
from app01.myModel import *
def index(request):
    if request.method=='GET':
        obj =UserForm()
        return render(request,'index.html',{'obj':obj})
    else:
        obj= UserForm(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            ret = Userinfo.objects.create(**obj.cleaned_data)
            print(ret.pk)
            return HttpResponse('添加成功')
        else:
            return render(request, 'index.html', locals())


def list(request):
    if request.method=='GET':
        user_list = Userinfo.objects.all()
        return render(request,'add.html',locals())

def edit(request,pk):
    pk=pk
    if request.method == 'GET':
        user = Userinfo.objects.filter(pk=pk).first()
        obj = UserForm(instance=user)
        return render(request,'edit.html',locals())
    else:
        obj = UserForm(request.POST)
        if obj.is_valid():
            Userinfo.objects.filter(pk=pk).update(**obj.cleaned_data)
            return redirect('/list/')
        else:
            return render(request,'edit.html',locals())

def delete(request,pk):
    Userinfo.objects.filter(pk=pk).delete()
    return redirect('/list/')