from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
import re
from django.conf import settings

class UserManager(BaseUserManager):
    def create_user(self, fullname, phone, password=None):
        if not re.fullmatch(r'\d{12}', str(phone)):
            raise ValueError('The Phone field must be a 12-digit number')

        user = self.model(
            fullname=fullname,
            phone=phone,
        )
        
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, fullname, phone, password=None):
        user = self.create_user(
            fullname=fullname,
            phone=phone,
            password=password
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class CUser(AbstractBaseUser, PermissionsMixin):
    fullname = models.CharField(verbose_name="نام و نام خانوادگی", max_length=60)
    phone = models.CharField(verbose_name="شماره تلفن", max_length=12, unique=True)
    address = models.TextField(verbose_name="نشانی", blank=True, null=True, default="", max_length=500)

    date_joined = models.DateField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)


    objects = UserManager()

    USERNAME_FIELD = 'phone'
    REQUIRED_FIELDS = ['fullname']

    def __str__(self):
        return self.phone

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_active

    class Meta:
        verbose_name = "اکانت"