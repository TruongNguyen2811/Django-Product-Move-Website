import django_filters
from websiteEndterm.models import *

class productFilter (django_filters.FilterSet):
    class Meta:
        model= product
        fields = '__all__'
        exclude={'ProductName', 'ProductLine','Describe'}

class produceFilter (django_filters.FilterSet):
    class Meta:
        model= produce
        fields = '__all__'
        exclude = {'idFactory','idProduct'}