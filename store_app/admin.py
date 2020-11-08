from django.contrib import admin

# Register your models here.

from store_app.models import Product, ProductFeature, CustomFeature, ProductType


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductFeature)
class ProductFeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(CustomFeature)
class CustomFeatureAdmin(admin.ModelAdmin):
    pass


@admin.register(ProductType)
class ProductTypeAdmin(admin.ModelAdmin):
    pass

