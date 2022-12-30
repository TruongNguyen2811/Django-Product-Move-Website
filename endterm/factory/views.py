from django.shortcuts import render, redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from websiteEndterm.serializers import GetAllFactory,GetAllProduce,GetAllProduct,GetAllClient,GetAllReceive,GetAllSell,GetAllStore,GetAllWarrantyCenter,GetAllWarranty
from websiteEndterm.models import product,factory,produce
from factory.filters import *
from .form import *
from django.core import serializers
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate,logout
from websiteEndterm.decorators import *
# Create your views here.
# def factorymain(request):
    # return HttpResponse("Hello world!")
    # template=loader.get_template('factory/produce.html')
    # return HttpResponse(template.render())
@login_required(login_url='/login')
@allowed_factory()
def factoryProduct(request):

    pk=request.user.factory.idFactory
    factorys=request.user.factory
    produces = produce.objects.filter(idFactory=pk)
    products=product.objects.filter(idFactory=pk, Describe= 'Cant fix')
    Recall=product.objects.filter(idFactory=pk, Describe= 'Product Recall')
    total_recall=Recall.count()
    total_warranty=products.count()
    on_sale= receive.objects.filter(idFactory=pk)
    total_onsale=on_sale.count()
    total_product=produces.count()
    myfilter1 = produceFilter(request.GET, queryset=produces)
    produces = myfilter1.qs
    myfilter2 = productFilter(request.GET, queryset=produces)
    produces = myfilter2.qs
    context={
        'total_recall':total_recall,
        'total_warranty':total_warranty,
        'produces':produces, 
        'total_product':total_product, 
        'factory':factorys, 
        'myfilter1':myfilter1,
        'myfilter2':myfilter2,
        'onsale':on_sale,
        'total_onsale':total_onsale,

    }
    return render(request,'factory/dashboard.html',context)

@login_required(login_url='/login')
@allowed_factory()
def CreateProduct(request,pk):
    formpro= ProductForm(initial={'Describe': 'New','idFactory': pk})
    factorys=factory.objects.get(idFactory=pk)
    if(request.method== 'POST'):
        formpro = ProductForm(request.POST)
        if formpro.is_valid():
            instance= formpro.save()
            return redirect('/factory/createproduce/'+pk)
    context = {
        'factory':factorys,
        'formpro':formpro,
    }
    return render(request,'factory/produce.html',context)

@login_required(login_url='/login')
@allowed_factory()
def createProduce(request, pk):
    factorys=factory.objects.get(idFactory=pk)
    formproduce=ProduceForm(initial={'idFactory': pk})
    if(request.method== 'POST'):
        formproduce = ProduceForm(request.POST)
        if formproduce.is_valid():
            formproduce.save()
            return redirect('/factory/')
    context = {
        'factory':factorys,
        'form':formproduce,
    }
    return render(request,'factory/createProduce.html',context)

@login_required(login_url='/login')
@allowed_factory()
def UpDateStatus(request, pkF,pkP):
    factorys=factory.objects.get(idFactory=pkF)
    pd=product.objects.get(idProduct=pkP)
    formrStatus=UpdateStatusForm(initial={'idFactory': pkF, 'idProduct':pkP, 'Describe':'On Sale'}, instance=pd)
    if(request.method== 'POST'):
        formrStatus = UpdateStatusForm(request.POST,instance=pd)
        if formrStatus.is_valid():
            formrStatus.save()
            return redirect('/factory/createreceive/'+pkF + '/'+pkP )
    context = {
        'factory':factorys,
        'form':formrStatus,
    }
    return render(request,'factory/CreateReceiveform.html',context)

@login_required(login_url='/login')
@allowed_factory()
def CreateReceive(request, pkF,pkP):
    factorys=factory.objects.get(idFactory=pkF)
    formrecieve=ReceiveForm(initial={'idFactory': pkF, 'idProduct':pkP})
    if(request.method== 'POST'):
        formrecieve = ReceiveForm(request.POST)
        if formrecieve.is_valid():
            formrecieve.save()
            return redirect('/factory/')
    context = {
        'factory':factorys,
        'form':formrecieve,
    }
    return render(request,'factory/CreateReceiveform.html',context)

@login_required(login_url='/login')
@allowed_factory()
def factoryWarrantyProduct(request,pk):
    factorys=factory.objects.get(idFactory=pk)
    produces = produce.objects.filter(idFactory=pk)
    products=product.objects.filter(idFactory=pk, Describe= 'Cant fix')
    products01=product.objects.filter(idFactory=pk, Describe= 'Cant fix')
    Recall=product.objects.filter(idFactory=pk, Describe= 'Product Recall')
    total_recall=Recall.count()
    total_warranty=products.count()
    # products=product.objects.filter(product.idProduct.idFactory==pk)
    total_product=produces.count()
    # total_product=produces.count()
    context={
        'total_recall':total_recall,
        'total_warranty':total_warranty,
        'products':products,
        'produces':produces, 
        'total_product':total_product, 
        'factory':factorys, 
        'products01':products01
        # 'myfilter1':myfilter1,
        # 'myfilter2':myfilter2,
    }
    return render(request,'factory/warranty.html',context)

@login_required(login_url='/login')
@allowed_factory()
def UpDateStatusDone (request, pkF,pkP):
    factorys=factory.objects.get(idFactory=pkF)
    pd=product.objects.get(idProduct=pkP)
    formrStatus=UpdateStatusForm(initial={'idFactory': pkF, 'idProduct':pkP, 'Describe':'Warranted'}, instance=pd)
    if(request.method== 'POST'):
        formrStatus = UpdateStatusForm(request.POST,instance=pd)
        if formrStatus.is_valid():
            formrStatus.save()
            return redirect('/factory/Updatewarranty/'+pkF + '/'+pkP )
    context = {
        'factory':factorys,
        'form':formrStatus,
    }
    return render(request,'factory/CreateReceiveform.html',context)

@login_required(login_url='/login')
@allowed_factory()
def UpDateWarranty (request, pkF,pkP):
    factorys=factory.objects.get(idFactory=pkF)
    pd=warranty.objects.get(idProduct=pkP)
    formrStatus=UpdateWarrantyForm(initial={ 'idProduct':pkP}, instance=pd)
    if(request.method== 'POST'):
        formrStatus = UpdateWarrantyForm(request.POST,instance=pd)
        if formrStatus.is_valid():
            formrStatus.save()
            return redirect('/factory/factoryWarranty/'+pkF )
    context = {
        'factory':factorys,
        'form':formrStatus,
    }
    return render(request,'factory/CreateReceiveform.html',context)

@login_required(login_url='/login')
@allowed_factory()
def factoryReCallProduct(request,pk):
    factorys=factory.objects.get(idFactory=pk)
    produces = produce.objects.filter(idFactory=pk)
    products=product.objects.filter(idFactory=pk, Describe= 'Cant fix')
    products01=product.objects.filter(idFactory=pk, Describe= 'Product Recall')
    Recall=product.objects.filter(idFactory=pk, Describe= 'Product Recall')
    total_recall=Recall.count()
    total_warranty=products.count()
    # products=product.objects.filter(product.idProduct.idFactory==pk)
    total_product=produces.count()
    # total_product=produces.count()
    context={
        'total_recall':total_recall,
        'total_warranty':total_warranty,
        'products':products,
        'produces':produces, 
        'total_product':total_product, 
        'factory':factorys, 
        'products01':products01
        # 'myfilter1':myfilter1,
        # 'myfilter2':myfilter2,
    }
    return render(request,'factory/warranty.html',context)

@login_required(login_url='/login')
@allowed_factory()
def DeleteProduct(request,pkF,pkP):
    products=product.objects.get(idProduct=pkP)
    if(request.method== 'POST'):
        products.delete()
        return redirect('/factory/factoryWarranty/'+pkF )
    context={
        'product':products
    }
    return render(request,'factory/delete.html',context)

@login_required(login_url='/login')
def logoutUser (request):
    logout(request)
    return redirect('/login/')