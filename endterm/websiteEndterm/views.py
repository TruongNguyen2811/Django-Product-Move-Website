from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import Group
from .models import factory, product,produce,store,receive,client,sell,warranty,warrantycenter
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate,logout
from .form import *
from .filters import *
from django.contrib import messages
# from websiteEndterm.models import factory
# from websiteEndterm.serializers import manageappleSerializer
# from rest_framework.decorators import api_view
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.decorators import login_required
from .decorators import *
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('/AdminDashBoard/')
    else:

        context = {
        }
        if(request.method== 'POST'):
            username=request.POST.get('username')
            password=request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/AdminDashBoard/')
            else:
                messages.info(request, 'Username or Password is incorrect')
                return render(request, 'login-register/login.html',context)
        return render(request,'login-register/login.html',context)


@login_required(login_url='/login')
@allowed_admin()
def registerAdmin(request):
    form=UserForm()
    if(request.method== 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            # user=form.cleaned_data.get('username')
            group = Group.objects.get(name='admins')
            user.groups.add(group)
            # messages.success(request, 'Hello.'+user)
            return redirect('/AdminForms/' )
    context = {
        'form':form,
    }
    return render(request,'login-register/register.html',context)


@login_required(login_url='/login')
@allowed_admin()
def registerFactory(request):
    form=UserForm()
    if(request.method== 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            # user=form.cleaned_data.get('username')
            group = Group.objects.get(name='factorys')
            user.groups.add(group)
            # messages.success(request, 'Hello.'+user)
            return redirect('/FactoryForms/' )
    context = {
        'form':form,
    }
    return render(request,'login-register/register.html',context)


@login_required(login_url='/login')
@allowed_admin()
def registerStore(request):
    form=UserForm()
    if(request.method== 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            # user=form.cleaned_data.get('username')
            group = Group.objects.get(name='Stores')
            user.groups.add(group)
            # messages.success(request, 'Hello.'+user)
            return redirect('/StoreForms/' )
    context = {
        'form':form,
    }
    return render(request,'login-register/register.html',context)


@login_required(login_url='/login')
@allowed_admin()
def registerWarrantyCenter(request):
    form=UserForm()
    if(request.method== 'POST'):
        form = UserForm(request.POST)
        if form.is_valid():
            user=form.save()
            # user=form.cleaned_data.get('username')
            group = Group.objects.get(name='warrantyCenters')
            user.groups.add(group)
            # messages.success(request, 'Hello.'+user)
            return redirect('/WarrantyCenterForms/' )
    context = {
        'form':form,
    }
    return render(request,'login-register/register.html',context)


@login_required(login_url='/login')
@allowed_admin()
def FactoryForms(request):
    form = Factoryform()
    if(request.method== 'POST'):
        form = Factoryform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/AdminDashBoard/' )
    context = {
        'form':form,
    }
    return render(request,'login-register/register.html',context)


@login_required(login_url='/login')
@allowed_admin()
def StoreForms(request):
    form = Storeform()
    if(request.method== 'POST'):
        form = Storeform(request.POST)
        if form.is_valid():
            form.save()
            # user=form.cleaned_data.get('username')
            # messages.success(request, 'Hello.'+user)
            return redirect('/AdminDashBoard/' )
    context = {
        'form':form,
    }
    return render(request,'login-register/register.html',context)


@login_required(login_url='/login')
@allowed_admin()
def WarrantyCenterForms(request):
    form = WarrantyCenterform()
    if(request.method== 'POST'):
        form = WarrantyCenterform(request.POST)
        if form.is_valid():
            form.save()
            # user=form.cleaned_data.get('username')
            # messages.success(request, 'Hello.'+user)
            return redirect('/AdminDashBoard/' )
    context = {
        'form':form,
    }
    return render(request,'login-register/register.html',context)

@login_required(login_url='/login')
@allowed_admin()
def AdminForms(request):
    form = Adminform()
    if(request.method== 'POST'):
        form = Adminform(request.POST)
        if form.is_valid():
            form.save()
            # user=form.cleaned_data.get('username')
            # messages.success(request, 'Hello.'+user)
            return redirect('/AdminDashBoard/' )
    context = {
        'form':form,
    }
    return render(request,'login-register/register.html',context)

# @allowed_users(allowed_roles=['admin'])
@login_required(login_url='/login')
def logoutUser (request):
    logout(request)
    return redirect('/login/')


@allowed_admin()
@login_required(login_url='/login')
# @only_admin
def AdminDashBoard(request):
    products=product.objects.all()
    total_products=products.count()
    factorys=factory.objects.all()
    total_factorys=factorys.count()
    stores=store.objects.all()
    total_stores=stores.count()
    warrantys=warranty.objects.all()
    total_warrantys=warrantys.count()
    Sold=sell.objects.all()
    total_sold=Sold.count()
    warrantyCenters=warrantycenter.objects.all()
    total_warrantyCenters=warrantyCenters.count()
    context = {
        'products':products,
        'total_products':total_products,
        'factorys':factorys,
        'total_factorys':total_factorys,
        'stores':stores,
        'total_stores':total_stores,
        'warrantys':warrantys,
        'total_warrantys':total_warrantys,
        'Sold':Sold,
        'total_sold':total_sold,
        'warrantyCenters':warrantyCenters,
        'total_warrantyCenters':total_warrantyCenters,

    }
    return render(request,'admin/dashboard.html',context)

@allowed_admin()
@login_required(login_url='/login')
# @only_admin
def AllFactory(request):
    products=product.objects.all()
    total_products=products.count()
    factorys=factory.objects.all()
    total_factorys=factorys.count()
    myfliter1= FactoryFilter(request.GET, queryset=factorys)
    factorys= myfliter1.qs
    total_factorys2=factorys.count()
    stores=store.objects.all()
    total_stores=stores.count()
    warrantys=warranty.objects.all()
    total_warrantys=warrantys.count()
    Sold=sell.objects.all()
    total_sold=Sold.count()
    warrantyCenters=warrantycenter.objects.all()
    total_warrantyCenters=warrantyCenters.count()
    produces = produce.objects.all()
    myfilter2 = produceFilter(request.GET, queryset=produces)
    produces = myfilter2.qs
    total_produces=produces.count()
    context = {
        'total2':total_factorys2,
        'myfilter1':myfliter1,
        'myfilter2':myfilter2,
        'produces':produces,
        'total_produces':total_produces,
        'products':products,
        'total_products':total_products,
        'factorys':factorys,
        'total_factorys':total_factorys,
        'stores':stores,
        'total_stores':total_stores,
        'warrantys':warrantys,
        'total_warrantys':total_warrantys,
        'Sold':Sold,
        'total_sold':total_sold,
        'warrantyCenters':warrantyCenters,
        'total_warrantyCenters':total_warrantyCenters,

    }
    return render(request,'admin/allFactory.html',context)

@allowed_admin()
@login_required(login_url='/login')
# @only_admin
def AllStores(request):
    products=product.objects.all()
    total_products=products.count()
    factorys=factory.objects.all()
    total_factorys=factorys.count()
    stores=store.objects.all()
    total_stores=stores.count()
    myfliter1= StoreFilter(request.GET, queryset=stores)
    stores= myfliter1.qs
    total_2=stores.count()
    warrantys=warranty.objects.all()
    total_warrantys=warrantys.count()
    Sold=sell.objects.all()
    total_sold=Sold.count()
    warrantyCenters=warrantycenter.objects.all()
    total_warrantyCenters=warrantyCenters.count()
    sells = sell.objects.all()
    myfilter2 = sellFilter(request.GET, queryset=sells)
    sells = myfilter2.qs
    total_sells=sells.count()
    context = {
        'total2':total_2,
        'myfilter1':myfliter1,
        'myfilter2':myfilter2,
        'sell':sells,
        'total_sells':total_sells,
        'products':products,
        'total_products':total_products,
        'factorys':factorys,
        'total_factorys':total_factorys,
        'stores':stores,
        'total_stores':total_stores,
        'warrantys':warrantys,
        'total_warrantys':total_warrantys,
        'Sold':Sold,
        'total_sold':total_sold,
        'warrantyCenters':warrantyCenters,
        'total_warrantyCenters':total_warrantyCenters,

    }
    return render(request,'admin/allStore.html',context)

@allowed_admin()
@login_required(login_url='/login')
# @only_admin
def AllWarrantyCenter(request):
    products=product.objects.all()
    total_products=products.count()
    factorys=factory.objects.all()
    total_factorys=factorys.count()
    stores=store.objects.all()
    total_stores=stores.count()
    warrantys=warranty.objects.all()
    total_warrantys=warrantys.count()
    myfilter2 = warrantyFilter(request.GET, queryset=warrantys)
    warrantys = myfilter2.qs
    total_1=warrantys.count()
    Sold=sell.objects.all()
    total_sold=Sold.count()
    warrantyCenters=warrantycenter.objects.all()
    total_warrantyCenters=warrantyCenters.count()
    myfliter1= WarrantyCenterFilter(request.GET, queryset=warrantyCenters)
    warrantyCenters= myfliter1.qs
    total_2=warrantyCenters.count()
    context = {
        'total2':total_2,
        'total1':total_1,
        'myfilter1':myfliter1,
        'myfilter2':myfilter2,
        'products':products,
        'total_products':total_products,
        'factorys':factorys,
        'total_factorys':total_factorys,
        'stores':stores,
        'total_stores':total_stores,
        'warrantys':warrantys,
        'total_warrantys':total_warrantys,
        'Sold':Sold,
        'total_sold':total_sold,
        'warrantyCenters':warrantyCenters,
        'total_warrantyCenters':total_warrantyCenters,

    }
    return render(request,'admin/allWarranty.html',context)

@allowed_admin()
@login_required(login_url='/login')
# @only_admin
def AllProduct(request):
    products=product.objects.all()
    total_products=products.count()
    myfliter1= TotalproductFilter(request.GET, queryset=products)
    products= myfliter1.qs
    total_2=products.count()
    factorys=factory.objects.all()
    total_factorys=factorys.count()
    stores=store.objects.all()
    total_stores=stores.count()
    warrantys=warranty.objects.all()
    total_warrantys=warrantys.count()
    myfilter2 = warrantyFilter(request.GET, queryset=warrantys)
    warrantys = myfilter2.qs
    total_1=warrantys.count()
    Sold=sell.objects.all()
    total_sold=Sold.count()
    warrantyCenters=warrantycenter.objects.all()
    total_warrantyCenters=warrantyCenters.count()
    context = {
        'total2':total_2,
        'total1':total_1,
        'myfilter1':myfliter1,
        'myfilter2':myfilter2,
        'products':products,
        'total_products':total_products,
        'factorys':factorys,
        'total_factorys':total_factorys,
        'stores':stores,
        'total_stores':total_stores,
        'warrantys':warrantys,
        'total_warrantys':total_warrantys,
        'Sold':Sold,
        'total_sold':total_sold,
        'warrantyCenters':warrantyCenters,
        'total_warrantyCenters':total_warrantyCenters,

    }
    return render(request,'admin/allProduct.html',context)