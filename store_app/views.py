from django.shortcuts import render


# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from store_app.serializers import ProductSerializer
from store_app.models import Product, ProductFeature, CustomFeature, ProductType


class ProductView(APIView):

    def get(self, request):
        r_type = request.query_params.get('type', None)
        if r_type is None:
            return Response(ProductSerializer(Product.objects.all(), many=True).data)
        else:
            return Response(ProductSerializer(Product.objects.all().filter(p_type__name=r_type), many=True).data)


    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save()
        return Response(ProductSerializer(instance).data)