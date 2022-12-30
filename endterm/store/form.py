from django.forms import ModelForm
from websiteEndterm.models import client,sell,product,receive,warranty


class ClientForm (ModelForm):
    class Meta:
        model = client
        fields = '__all__'
        # exclude ={'idFactory'}

class OrderForm (ModelForm):
    class Meta:
        model = sell
        fields = '__all__'
class ProductForm (ModelForm):
    class Meta:
        model = product
        fields = '__all__'

class warrantyform(ModelForm):
    class Meta:
        model = warranty
        fields = '__all__'

class ReciveForm(ModelForm):
    class Meta:
        model = receive
        fields = '__all__'

