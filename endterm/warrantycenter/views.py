from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from websiteEndterm.serializers import GetAllFactory,GetAllProduce,GetAllProduct,GetAllClient,GetAllReceive,GetAllSell,GetAllStore,GetAllWarrantyCenter,GetAllWarranty
from websiteEndterm.models import product,factory,produce
from .filters import *
from .form import *
from django.contrib.auth import login, authenticate,logout
from django.core import serializers
from django.contrib.auth.decorators import login_required
from websiteEndterm.decorators import *
# Create your views here.
# def factorymain(request):
    # return HttpResponse("Hello world!")
    # template=loader.get_template('factory/produce.html')
    # return HttpResponse(template.render())

@login_required(login_url='/login')
@allowed_WarrantyCenter()
def WarrantyDashBoard(request):
    pk=request.user.warrantycenter.idWarrantyCenter
    warrantycenters=request.user.warrantycenter
    Products = warranty.objects.filter(idWarrantyCenter=pk,Status='Warranting')
    moveTofactory=warranty.objects.filter(idWarrantyCenter=pk,Status='Cant fix')
    total_move=moveTofactory.count()
    clients = client.objects.all()
    warrantys=warranty.objects.filter(idWarrantyCenter=pk)
    total_warrantys=warrantys.count()
    total_product=Products.count()
    myfilter1 = ClientFilter(request.GET, queryset=clients)
    clients = myfilter1.qs
    myfilter2 = WarrantingFilter(request.GET, queryset=Products)
    Products = myfilter2.qs
    context = {
        'Product':Products, 
        'total_product':total_product, 
        'warrantycenter':warrantycenters,
        'total_move':total_move,
        # 'store':stores,
        'warrantys':warrantys,
        'myfilter1':myfilter1,
        'myfilter2':myfilter2,
        'client':clients,
        'total_warrantys':total_warrantys
    }
    return render(request,'warrantycenter/dashboard.html',context)

@login_required(login_url='/login')
@allowed_WarrantyCenter()
def ClientsDetail(request,pkW,pkC):
    warrantycenters= warrantycenter.objects.get(idWarrantyCenter=pkW)
    clients = client.objects.get(idClient=pkC)
    warrantys = warranty.objects.filter(idWarrantyCenter=pkW)
    total_warrantys=warrantys.count()
    sells=sell.objects.filter(idClient=pkC)
    total_sells=sells.count()
    context={
        'warrantyCenters':warrantycenters,
        'client':clients,
        'total_warrantys':total_warrantys,
        'sell':sells,
        'total_sells':total_sells,
    }
    return render(request,'warrantycenter/clientview.html',context)

@login_required(login_url='/login')
@allowed_WarrantyCenter()
def UpDateStatus(request, pkW,pkP):
    warrantycenters= warrantycenter.objects.get(idWarrantyCenter=pkW)
    pd=product.objects.get(idProduct=pkP)
    formrStatus=UpdateStatusForm(initial={ 'idProduct':pkP, 'Describe':'Warranting'}, instance=pd)
    if(request.method== 'POST'):
        formrStatus = UpdateStatusForm(request.POST,instance=pd)
        if formrStatus.is_valid():
            formrStatus.save()
            return redirect('/warrantycenter/CreateWarranty/'+pkW + '/'+pkP )
    context = {
        'warrantycenters':warrantycenters,
        'form':formrStatus,
    }
    return render(request,'factory/CreateReceiveform.html',context)

@login_required(login_url='/login')
@allowed_WarrantyCenter()
def UpDateWarranty(request, pkW,pkP):
    warrantycenters= warrantycenter.objects.get(idWarrantyCenter=pkW)
    formrStatus=WarrantyForm(initial={ 'idProduct':pkP, 'idWarrantyCenter':pkW})
    if(request.method== 'POST'):
        formrStatus = WarrantyForm(request.POST)
        if formrStatus.is_valid():
            formrStatus.save()
            return redirect('/warrantycenter/' )
    context = {
        'warrantycenters':warrantycenters,
        'form':formrStatus,
    }
    return render(request,'factory/CreateReceiveform.html',context)

@login_required(login_url='/login')
@allowed_WarrantyCenter()
def UpdateDoneProduct(request, pkW,pkP):
    warrantycenters= warrantycenter.objects.get(idWarrantyCenter=pkW)
    pd=product.objects.get(idProduct=pkP)
    formrStatus=UpdateStatusForm(initial={ 'idProduct':pkP, 'Describe':'Warranted'}, instance=pd)
    if(request.method== 'POST'):
        formrStatus = UpdateStatusForm(request.POST,instance=pd)
        if formrStatus.is_valid():
            formrStatus.save()
            return redirect('/warrantycenter/updatesWarrantedWarranty/'+pkW + '/'+pkP )
    context = {
        'warrantycenters':warrantycenters,
        'form':formrStatus,
    }
    return render(request,'factory/CreateReceiveform.html',context)

@login_required(login_url='/login')
@allowed_WarrantyCenter()
def UpDateWarrantyinWarranty(request, pkW,pkP):
    warrantycenters= warrantycenter.objects.get(idWarrantyCenter=pkW)
    pd=warranty.objects.get(idProduct=pkP,Status='Warranting')
    formrStatus=WarrantyForm(initial={ 'idProduct':pkP, 'idWarrantyCenter':pkW}, instance=pd)
    if(request.method== 'POST'):
        formrStatus = WarrantyForm(request.POST,instance=pd)
        if formrStatus.is_valid():
            formrStatus.save()
            return redirect('/warrantycenter/')
    context = {
        'warrantycenters':warrantycenters,
        'form':formrStatus,
    }
    return render(request,'factory/CreateReceiveform.html',context)

@login_required(login_url='/login')
@allowed_WarrantyCenter()
def MoveBackProduct(request,pk):
    warrantycenters=warrantycenter.objects.get(idWarrantyCenter=pk)
    moveTofactory=warranty.objects.filter(idWarrantyCenter=pk,Status='Cant fix')
    data=warranty.objects.filter(idWarrantyCenter=pk,Status='Cant fix')
    total_move=moveTofactory.count()
    warrantys=warranty.objects.filter(idWarrantyCenter=pk)
    total_warrantys=warrantys.count()
    myfilter2 = WarrantingFilter(request.GET, queryset=data)
    data = myfilter2.qs
    total_data=data.count()
    context = {
        # 'Product':Products, 
        # 'total_product':total_product, 
        'warrantycenter':warrantycenters,
        'total_move':total_move,
        # 'store':stores,
        'data':data,
        'total_data':total_data,
        'warrantys':warrantys,
        'myfilter2':myfilter2,
        'total_warrantys':total_warrantys
    }
    return render(request,'warrantycenter/productview.html',context)

@login_required(login_url='/login')
@allowed_WarrantyCenter()
def AllWarrantyProduct(request,pk):
    warrantycenters=warrantycenter.objects.get(idWarrantyCenter=pk)
    moveTofactory=warranty.objects.filter(idWarrantyCenter=pk,Status='Cant fix')
    data=warranty.objects.filter(idWarrantyCenter=pk)
    total_move=moveTofactory.count()
    warrantys=warranty.objects.filter(idWarrantyCenter=pk)
    total_warrantys=warrantys.count()
    myfilter2 = WarrantingFilter(request.GET, queryset=data)
    data = myfilter2.qs
    total_data=data.count()
    context = {
        # 'Product':Products, 
        # 'total_product':total_product, 
        'warrantycenter':warrantycenters,
        'total_move':total_move,
        # 'store':stores,
        'data':data,
        'total_data':total_data,
        'warrantys':warrantys,
        'myfilter2':myfilter2,
        'total_warrantys':total_warrantys
    }
    return render(request,'warrantycenter/productview.html',context)


# Create your views here.
