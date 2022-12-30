from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from django.template import loader
from websiteEndterm.models import product,factory,produce
from factory.filters import *
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
@allowed_Store()
def StoreDashBoard(request):
    pk=request.user.store.idStore
    stores=request.user.store
    Products = receive.objects.filter(idStore=pk)
    clients = client.objects.all()
    sells=sell.objects.filter(idStore=pk)
    total_sell=sells.count()
    total_product=Products.count()
    # myfilter1 = produceFilter(request.GET, queryset=produces)
    # produces = myfilter1.qs
    # myfilter2 = productFilter(request.GET, queryset=produces)
    # produces = myfilter2.qs
    context = {
        'Product':Products, 
        'total_product':total_product, 
        'store':stores,
        'client':clients,
        'total_sell':total_sell
    }
    return render(request,'store/dashboard.html',context)

@login_required(login_url='/login')
@allowed_Store()
def recall(request,pkS,pkP):
    stores=store.objects.get(idStore=pkS)
    products=product.objects.get(idProduct=pkP)
    # receives=receive.objects.get(idProduct=pkP)
    recallform=ProductForm(initial={ 'idProduct':pkP,'Describe':'Product Recall'}, instance=products)
    if(request.method== 'POST'):
        recallform = ProductForm(request.POST,instance=products)
        if recallform.is_valid():
            recallform.save()
            # receives.delete()
            return redirect('/store/recallToWarranty/'+pkS +'/'+pkP)
    context = {
        'store':stores,
        'NewClientForm':recallform,
    }
    return render(request,'store/NewClientForm.html',context)

@login_required(login_url='/login')
@allowed_Store()
def recallToWarranty(request,pkS,pkP):
    stores=store.objects.get(idStore=pkS)
    recallform=warrantyform(initial={ 'idProduct':pkP,'Status':'Warranting'},)
    if(request.method== 'POST'):
        recallform = warrantyform(request.POST)
        if recallform.is_valid():
            recallform.save()
            return redirect('/store/' )
    context = {
        'store':stores,
        'NewClientForm':recallform,
    }
    return render(request,'store/NewClientForm.html',context)

@login_required(login_url='/login')
@allowed_Store()
def StoreSoldBoard(request,pk):
    stores=store.objects.get(idStore=pk)
    Products = receive.objects.filter(idStore=pk)
    clients = client.objects.all()
    sells=sell.objects.filter(idStore=pk)
    total_sell=sells.count()
    # products=product.objects.filter(product.idProduct.idFactory==pk)
    total_product=Products.count()
    # myfilter1 = produceFilter(request.GET, queryset=produces)
    # produces = myfilter1.qs
    # myfilter2 = productFilter(request.GET, queryset=produces)
    # produces = myfilter2.qs
    # total_product=produces.count()
    context = {
        'Product':Products, 
        'total_product':total_product, 
        'store':stores,
        'client':clients,
        'sells':sells,
        'total_sell':total_sell
    }
    return render(request,'store/allProduct.html',context)

@login_required(login_url='/login')
@allowed_Store()
def AddNewClient(request,pk):
    NewClientForm= ClientForm()
    stores=store.objects.get(idStore=pk)
    if(request.method== 'POST'):
        NewClientForm = ClientForm(request.POST)
        if NewClientForm.is_valid():
            instance= NewClientForm.save()
            return redirect('/store/')
    context = {
        'store':stores,
        'NewClientForm':NewClientForm,
    }
    return render(request,'store/NewClientForm.html',context)

@login_required(login_url='/login')
@allowed_Store()
def SoldStatus(request,pkS,pkP):
    stores=store.objects.get(idStore=pkS)
    products=product.objects.get(idProduct=pkP)
    # receives=receive.objects.get(idProduct=pkP)
    recallform=ProductForm(initial={ 'idProduct':pkP,'Describe':'Sold'}, instance=products)
    if(request.method== 'POST'):
        recallform = ProductForm(request.POST,instance=products)
        if recallform.is_valid():
            recallform.save()
            # receives.delete()
            return redirect('/store/neworderform/'+pkS +'/'+pkP)
    context = {
        'store':stores,
        'NewClientForm':recallform,
    }
    return render(request,'store/NewClientForm.html',context)

@login_required(login_url='/login')
@allowed_Store()
def AddNewOrder(request,pk):
    NewOrderForm= OrderForm(initial={'idStore': pk})
    stores=store.objects.get(idStore=pk)
    if(request.method== 'POST'):
        NewOrderForm = OrderForm(request.POST)
        if NewOrderForm.is_valid():
            instance= NewOrderForm.save()
            return redirect('/store/')
    context = {
        'store':stores,
        'NewOrderForm':NewOrderForm,
    }
    return render(request,'store/NewOrderForm.html',context)

@login_required(login_url='/login')
@allowed_Store()
def ClientsDetails(request,pkS,pkC):
    stores= store.objects.get(idStore=pkS)
    clients = client.objects.get(idClient=pkC)
    Products = receive.objects.filter(idStore=pkS)
    total_product=Products.count()
    sells=sell.objects.filter(idClient=pkC)
    total_sells=sells.count()
    context={
        'store':stores,
        'client':clients,
        'total_product':total_product,
        'sell':sells,
        'total_sells':total_sells,
    }
    return render(request,'store/clientview.html',context)


@login_required(login_url='/login')
def logoutUser (request):
    logout(request)
    return redirect('/login/')
# Create your views here.
