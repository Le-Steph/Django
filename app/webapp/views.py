from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response 
from rest_framework import status 
from webapp.models import *
from webapp.serializers import *


class farmerList(APIView):

    def get(self, request):
        farmer1 = farmer.objects.all() 
        serializer = farmerSerializer(farmer1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class productList(APIView):

    def get(self, request):
        product1 = product.objects.all()
        serializer = productSerializer(product1, many=True)
        return Response(serializer.data)

    def post(self):
        pass

class certificateList(APIView):

    def get(self, request):
        certificate1 = certificate.objects.all()
        #certificate1 = certificate1.objects.filter(types="biologique")
        serializer = certificateSerializer(certificate1, many=True)
        return Response(serializer.data)

    def post(self):
        pass