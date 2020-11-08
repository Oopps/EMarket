from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from store_app.models import Product, ProductFeature, CustomFeature, ProductType


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=64)
    description = serializers.CharField(max_length=512)
    price = serializers.FloatField()
    weight = serializers.FloatField()
    p_type = serializers.StringRelatedField(read_only=True)


    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        Product.objects.filter(pk=instance.id).update(**validated_data)
        return Product.objects.get(pk=instance.pk)