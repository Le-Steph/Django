from rest_framework import serializers 
from webapp.models import *


class farmerSerializer(serializers.ModelSerializer):


    class Meta:
        model = farmer
        fields =('nom')

    class Meta:
        model = farmer
        fields =('numero_siret') 

    class Meta:
        model = farmer
        fields =('adresse')
    
    class Meta:
        model = farmer
        fields ='__all__'


class productSerializer(serializers.ModelSerializer):


    class Meta:
        model = product
        fields =('nom')

    class Meta:
        model = product
        fields =('unite') 

    class Meta:
        model = product
        fields =('codification')
    
    class Meta:
        model = product
        fields =('producteurs')
    
    class Meta:
        model = product
        fields ='__all__'

    
class certificateSerializer(serializers.ModelSerializer):


    class Meta:
        model = certificate
        fields =('nom')

    class Meta:
        model = certificate
        fields =('types') 

    class Meta:
        model = certificate
        fields =('farmer_certif')
    
    class Meta:
        model = certificate
        fields ='__all__'