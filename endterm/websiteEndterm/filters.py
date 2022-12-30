import django_filters
from websiteEndterm.models import *

class TotalproductFilter (django_filters.FilterSet):
    class Meta:
        model= product
        fields = '__all__'
        exclude={'Describe'}

class FactoryFilter (django_filters.FilterSet):
    class Meta:
        model= factory
        fields = '__all__'
        exclude={'user', 'FactoryAddress'}

class produceFilter (django_filters.FilterSet):
    class Meta:
        model= produce
        fields = '__all__'
        exclude = {'idProduct', 'DateOfManuFacture'}

class StoreFilter (django_filters.FilterSet):
    class Meta:
        model= store
        fields = '__all__'
        exclude={'user', 'StoreAddress'}

class sellFilter (django_filters.FilterSet):
    class Meta:
        model= sell
        fields = '__all__'
        exclude={'idClient', 'idProduct','WarrantyPeriod'}

class warrantyFilter (django_filters.FilterSet):
    class Meta:
        model= warranty
        fields = '__all__'
        exclude={'idProduct'}

class WarrantyCenterFilter (django_filters.FilterSet):
    class Meta:
        model= warrantycenter
        fields = '__all__'
        exclude={'user', 'WarrantyCenterAddress'}