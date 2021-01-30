
from django.db import models
from  django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, email, password, first_name, last_name, is_admin=False):
        if not email:
            raise ValueError("Users must have an email address")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(email = self.normalize_email(email))
        user_obj.set_password(password)
        user_obj.first_name = first_name
        user_obj.last_name = last_name
        user_obj.is_admin = False
        user_obj.has_module_perms = True
        user_obj.save(using=self._db)
        return user_obj

    def create_superuser(self, email, password, first_name, last_name):
        user = self.create_user(email = self.normalize_email(email), password=password, first_name=first_name, last_name=last_name)
        user.is_admin = True 
        user.is_superuser = True 
        user.is_staff = True
        user.has_module_perms = True

        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True, max_length=255)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_admin = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['password', 'first_name', 'last_name']
    objects = UserManager()
   
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
    def __str__(self):
    	return self.email