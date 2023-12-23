from django.shortcuts import render
from rest_framework import viewsets
from app1.models import Product
from app1.serializers import ProductSerializer
from rest_framework.response import Response

# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer