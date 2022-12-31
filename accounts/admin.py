from django.contrib import admin
from  .models import Account
from django.contrib.auth.admin import UserAdmin
from .models import Account,Profile,Ip
# Register your models here.
@admin.register(Account)
class AcountAdmin(UserAdmin):
    list_display=['email','username','phone_number']
    list_filter=()
    filter_horizontal=()
    fieldsets=()

@admin.register(Profile)
class Profile(admin.ModelAdmin):
    list_display=['user']
    search_fields = ['user','full_name']

@admin.register(Ip)
class Ip(admin.ModelAdmin):
    list_display=['ip']
