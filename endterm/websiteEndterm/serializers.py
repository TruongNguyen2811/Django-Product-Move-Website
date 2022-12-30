from rest_framework import serializers
from .models import factory, product,produce,store,receive,client,sell,warranty,warrantycenter

class GetAllFactory(serializers.ModelSerializer):
    class Meta:
        model=factory
        fields = "__all__"

    def validate_FactoryPhone(self,value):
        x=0
        for i in value:
            if(i <"0"or i >"9"):
                x=x+1
        if(len(value)<10 or x>0):
            raise serializers.ValidationError("Wrong Phone Number")
        else:
            return value
    
    def validate_idFactory(self,value):
        if(len(value)<5):
            raise serializers.ValidationError("Wrong Id Factory")
        else:
            return value
    
    def validate_FactoryName(self,value):
        return value

    def validate_FactoryAddress(self,value):
        return value
           

class GetAllProduct(serializers.ModelSerializer):
    class Meta:
        model=product
        fields = "__all__"

    def validate_idProduct(self,value):
        if(len(value)<9):
            raise serializers.ValidationError("Wrong Id Product")
        else:
            return value
    
    # def validate(self,value):
    #     if(data['ProductLine']=='Iphone'):
    #         for i in range(2):
    #             ifpy
    
    def validate_ProductLine(self,value):
        if (value == 'Iphone' or value == 'AirPods' or value == 'MacBook' or value == 'Ipad' or value=='Watch' or value =='TV&Home'):
            return value
        else:
            raise serializers.ValidationError("Wrong Product Line")
    
    def validate_Describe(self,value):
        if(value == 'new' or value == 'sold'or value =='warranted'):
            return value
        else:
            raise serializers.ValidationError("Wrong describe")


class GetAllProduce(serializers.ModelSerializer):
    class Meta:
        model=produce
        fields = "__all__"

class GetAllStore(serializers.ModelSerializer):
    class Meta:
        model=store
        fields = "__all__"

class GetAllReceive(serializers.ModelSerializer):
    class Meta:
        model=receive
        fields = "__all__"

class GetAllClient(serializers.ModelSerializer):
    class Meta:
        model=client
        fields = "__all__"

class GetAllSell(serializers.ModelSerializer):
    class Meta:
        model=sell
        fields = "__all__"

class GetAllWarranty(serializers.ModelSerializer):
    class Meta:
        model=warranty
        fields = "__all__"

class GetAllWarrantyCenter(serializers.ModelSerializer):
    class Meta:
        model=warrantycenter
        fields = "__all__"
