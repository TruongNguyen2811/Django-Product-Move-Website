from __future__ import unicode_literals

from django.db import models

# Create your models here.

# tạo cơ sở dữ liệu cho phần tài khoản
from django.contrib.auth.models import User
class admin(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    idAdmin= models.CharField(max_length=10,primary_key=True, blank=False, null=False)
    AdminName=models.CharField(max_length=100, blank=False,null=False)
    AdminPhone=models.CharField(max_length=10,blank=False,null=False)

class factory(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    idFactory= models.CharField(max_length=10,primary_key=True, blank=False, null=False)
    FactoryName=models.CharField(max_length=100, blank=False,null=False)
    FactoryAddress=models.CharField(max_length=250,blank=False,null=False)
    FactoryPhone=models.CharField(max_length=10,blank=False,null=False)
    def __str__(self):
        return self.idFactory

class product(models.Model):
    idFactory=models.ForeignKey(factory,on_delete=models.CASCADE)
    idProduct=models.CharField(max_length=20,primary_key=True,blank=False,null=False)
    ProductName=models.CharField(max_length=50,blank=False,null=False)
    PRODUCTLINE=(
        ('Iphone','Iphone'),
        ('Airpods','Airpods'),
        ('MacBook','MacBook'),
        ('Ipad','Ipad'),
        ('Watch','Watch'),
        ('TV&Home','TV&Home'),
    )
    DESCRIBE=(
        ('New','New'),
        ('Sold','Sold'),
        ('Warranting','Warranting'),
        ('Warranted','Warranted'),
        ('Cant fix' , 'Cant fix'),
        ('Product Recall','Product Recall'),
        ('On Sale', 'On sale')
    )
    ProductLine=models.CharField(max_length=50,blank=False,null=False,choices=PRODUCTLINE)
    # BatchOfGoods=models.CharField(max_length=35,blank=False,null=False)
    Describe=models.CharField(max_length=500,blank=False,null=False,choices=DESCRIBE)
    
    objects = models.Manager()

    def __str__(self):
        return self.idProduct

class produce(models.Model):
    idFactory=models.ForeignKey(factory,on_delete=models.CASCADE)
    idProduct=models.ForeignKey(product,on_delete=models.CASCADE,unique=True)
    DateOfManuFacture=models.DateField(blank=False,null=False)
    WareHouse=models.CharField(max_length=250,blank=False,null=False)

class store(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    idStore= models.CharField(max_length=10,primary_key=True, blank=False, null=False)
    StoreName=models.CharField(max_length=100, blank=False,null=False)
    StoreAddress=models.CharField(max_length=250,blank=False,null=False)
    StorePhone=models.CharField(max_length=10,blank=False,null=False)
    def __str__(self):
        return self.idStore

class receive(models.Model):
    idFactory=models.ForeignKey(factory,on_delete=models.CASCADE)
    idStore=models.ForeignKey(store,on_delete=models.CASCADE)
    idProduct=models.ForeignKey(product,on_delete=models.CASCADE,unique=True)
    ReceivedDate=models.DateField(blank=False,null=False)
    StoreWareHouse=models.CharField(max_length=250,blank=False,null=False)

class client(models.Model):
    idClient=models.CharField(max_length=20,primary_key=True,blank=False,null=False)
    ClientName=models.CharField(max_length=100, blank=False,null=False)
    PhoneNumber=models.CharField(max_length=10,blank=False,null=False)
    def __str__(self):
        return self.idClient

class sell(models.Model):
    idClient=models.ForeignKey(client,on_delete=models.CASCADE)
    idStore=models.ForeignKey(store,on_delete=models.CASCADE)
    idProduct=models.ForeignKey(product,on_delete=models.CASCADE,unique=True)
    SellDate=models.DateField(blank=False,null=False)
    WarrantyPeriod=models.DateField(blank=False,null=False)

class warrantycenter(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    idWarrantyCenter= models.CharField(max_length=10,primary_key=True, blank=False, null=False)
    WarrantyCenterName=models.CharField(max_length=100, blank=False,null=False)
    WarrantyCenterAddress=models.CharField(max_length=250,blank=False,null=False)
    WarrantyCenterPhone=models.CharField(max_length=10,blank=False,null=False)
    def __str__(self):
        return self.idWarrantyCenter

class warranty(models.Model):
    idProduct=models.ForeignKey(product,on_delete=models.CASCADE)
    idWarrantyCenter=models.ForeignKey(warrantycenter,on_delete=models.CASCADE)
    WarrantyDate=models.DateField(blank=False,null=False)
    STATUS=(
        ('Warranting','Warranting'),
        ('Cant fix' , 'Cant fix'),
        ('Done','Done'),
    )
    Status=models.CharField(max_length=500,blank=False,null=False,choices=STATUS)
    Error=models.CharField(max_length=500)
