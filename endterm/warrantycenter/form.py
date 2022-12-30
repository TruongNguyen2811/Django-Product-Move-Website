from django.forms import ModelForm
from websiteEndterm.models import warranty,product


class WarrantyForm (ModelForm):
    class Meta:
        model = warranty
        fields = '__all__'
        # exclude ={'idFactory'}
class UpdateStatusForm (ModelForm):
    class Meta:
        model = product
        fields = '__all__'
        exclude = {'idFactory','ProductLine', 'ProductName'}
