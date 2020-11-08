from django.db import models

# Create your models here.


class ProductType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField(max_length=512)
    price = models.FloatField()
    weight = models.FloatField()
    p_type = models.ForeignKey(ProductType, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.name


class CustomFeature(models.Model):
    name = models.CharField(max_length=32)


    def __str__(self):
        return self.name


class ProductFeature(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    feature = models.ForeignKey(CustomFeature, on_delete=models.CASCADE)
    value = models.CharField(max_length=64, default='')

    def __str__(self):
        return str(self.product) + ' - ' + str(self.feature) + ': ' + self.value





