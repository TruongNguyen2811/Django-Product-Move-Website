import django_filters
from websiteEndterm.models import *

class ClientFilter (django_filters.FilterSet):
    class Meta:
        model= client
        fields = '__all__'
        exclude={'idClient', 'ClientName'}

class WarrantingFilter (django_filters.FilterSet):
    class Meta:
        model= warranty
        fields = '__all__'
        exclude = { 'idWarrantyCenter', 'Status' , 'Error'}