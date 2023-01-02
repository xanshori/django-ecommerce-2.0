from django.db import models
from category.models import SubCategories
from accounts.models import MerchantUser
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from uuid import uuid4
# Create your models here.

class Products(models.Model):
    id=models.UUIDField(default=uuid4,primary_key=True,unique=True,editable=False)
    subcategories_id=models.ForeignKey(SubCategories,on_delete=models.CASCADE)
    product_name=models.CharField(max_length=255)
    slug = models.SlugField(_("slug"))
    brand=models.CharField(max_length=255)
    product_max_price=models.CharField(max_length=255)
    product_discount_price=models.CharField(max_length=255)
    product_description=models.TextField()
    product_long_description=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    added_by_merchant=models.ForeignKey(MerchantUser,on_delete=models.CASCADE)
    in_stock_total=models.BooleanField(default=True)
    is_active=models.BooleanField(default=True)

    def save(self):
        self.slug = slugify(self.product_name)
        super(Products,self).save()

class ProductDetails(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    title_details=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

class ProductTags(models.Model):
    id=models.AutoField(primary_key=True)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

class ProductVarient(models.Model):
    id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)

class ProductVarientItems(models.Model):
    id=models.AutoField(primary_key=True)
    product_varient_id=models.ForeignKey(ProductVarient,on_delete=models.CASCADE)
    product_id=models.ForeignKey(Products,on_delete=models.CASCADE)
    title=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)


    'https://github.com/hackstarsj/django-ecommerce-project-amazon-clone'