from django.contrib import admin
from product.models import Products,ProductDetails,ProductTags,ProductVarient,ProductVarientItems
# Register your models here.

@admin.register(Products)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["product_name","product_max_price",
        "product_description","slug","product_max_price",
        "product_discount_price","product_long_description",
        "created_at","in_stock_total","is_active"
    ]
    readonly_fields = ["slug","created_at"]


@admin.register(ProductDetails)
class ProductDetailsAdmin(admin.ModelAdmin):
    list_display = ["title","title_details","created_at","is_active"]


@admin.register(ProductTags)
class ProductTagsAdmin(admin.ModelAdmin):
    list_display = ["title","created_at","is_active"]


@admin.register(ProductVarient)
class ProductVarientAdmin(admin.ModelAdmin):
    list_display = ["title","created_at"]


@admin.register(ProductVarientItems)
class ProductVarientItemsAdmin(admin.ModelAdmin):
    list_display = ["title","created_at"]