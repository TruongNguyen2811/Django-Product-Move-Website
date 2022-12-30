from django.forms import ModelForm
from websiteEndterm.models import produce, product, receive,warranty


class ProduceForm (ModelForm):
    class Meta:
        model = produce
        fields = '__all__'
        # exclude ={'idFactory'}
class ProductForm (ModelForm):
    class Meta:
        model = product
        fields = '__all__'
class ReceiveForm (ModelForm):
    class Meta:
        model = receive
        fields = '__all__'
class UpdateStatusForm (ModelForm):
    class Meta:
        model = product
        fields = '__all__'
        exclude = {'idFactory','ProductLine', 'ProductName'}
class UpdateWarrantyForm (ModelForm):
    class Meta:
        model = warranty
        fields = '__all__'
        # exclude = {'idFactory','ProductLine', 'ProductName'}
