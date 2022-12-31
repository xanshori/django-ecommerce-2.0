from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.

class MyAccountManager(BaseUserManager):
    def create_user(self,first_name,last_name,username,email,phone_number,password=None):
        if not email:
            raise ValueError("user must be have an email")
        if not username:
            raise ValueError("user must be have an username")
        user = self.model(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,first_name,last_name,username,email,phone_number,password):
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            username=username,
            email=self.normalize_email(email),
            phone_number=phone_number,
            password=password,
        )
        user.is_active=True
        user.is_staff=True
        user.is_admin=True
        user.is_superuser=True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser,PermissionsMixin):
    username        = models.CharField(max_length=50,unique=True)
    first_name      = models.CharField(_("first name"), max_length=50)
    last_name       = models.CharField(_("last name"), max_length=50)
    email           = models.EmailField(unique=True)
    phone_number    = models.CharField(max_length=20)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now=True)

    objects = MyAccountManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username","phone_number"]

    def __str__(self):
        return self.email


class Ip(models.Model):
    ip              = models.CharField(max_length=20,blank=True,null=True)
    class Meta:
        verbose_name_plural = 'Ip'
class Profile(models.Model):
    user            = models.OneToOneField(Account,on_delete=models.CASCADE)
    first_name      = models.CharField(_("first name"), max_length=50)
    last_name       = models.CharField(_("last name"), max_length=50)
    tanggal_lahir   = models.DateField(null=True,blank=True)
    phone_number    = models.CharField(max_length=20)
    profile_picture = models.ImageField(blank=True,null=True,upload_to='media/profiles/',default="profiles/default.png")
    ip              = models.ForeignKey(Ip,on_delete=models.CASCADE,blank=True,null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    def full_name(self):
        return f"{self.first_name} {self.last_name}"


class PhysicalAddresses(models.Model):
    user            = models.ForeignKey(Profile,on_delete=models.CASCADE,blank=True,null=True)
    full_address    = models.CharField(max_length=225)
    city            = models.CharField(max_length=255)
    province        = models.CharField(max_length=255)
    country         = models.CharField(max_length=255)
    postal_code     = models.CharField(max_length=10)
    is_active       = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.user.first_name}"