from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractBaseUser,PermissionsMixin
# Create your models here.
class MyUserManager(BaseUserManager):
    def _create_user(self,email,first_name,last_name,password,**extra_fields):
        if not email:
            raise ValueError('Email is required')
        if not first_name:
            raise ValueError('First name is required')
        if not last_name:
            raise ValueError('Last name is required')

        user = self.model(
            email = self.normalize_email(email),
            first_name = first_name,
            last_name = last_name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_user(self,email,first_name,last_name,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',False)
        return self._create_user(email,first_name,last_name,password,**extra_fields)

    def create_superuser(self,email,first_name,last_name,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_active',True)
        extra_fields.setdefault('is_superuser',True)
        return self._create_user(email,first_name,last_name,password,**extra_fields)

class MyUser(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    objects = MyUserManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name','last_name']

    def __str__(self):
        return f'{self.first_name},{self.last_name}'


# class MyUserManager(BaseUserManager):
#     def _create_user(self,email,first_name,last_name,password = None):
#         if not email:
#             raise ValueError('email is required')
#         if not first_name:
#             raise ValueError('first name is required')
#         if not last_name:
#             raise ValueError('last name is required')

#         user =self.model(
#             email = self.normalize_email(email),
#             first_name = first_name,
#             last_name = last_name
#         )
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
        
#     def create_superuser(self,email,first_name,last_name,password = None):
#         user = self.create_superuser(
#             email = self.normalize_email(email),
#             first_name=first_name,
#             last_name=last_name,
#             password=password
#         )
#         user.is_admin = True
#         user.is_superuser = True
#         user.save(using=self._db)
#         return user

# class MyUser(AbstractBaseUser):
#     email = models.EmailField(unique=True)
#     first_name = models.CharField(max_length=150)
#     last_name = models.CharField(max_length=150)
#     is_admin = models.BooleanField(default=True)
#     is_active = models.BooleanField(default=True)
#     is_staff = models.BooleanField(default=True)
#     is_superuser = models.BooleanField(default=True)
    
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = ('first_name',"last_name")
#     objects = MyUserManager()

#     def __str__(self):
#         return f'{self.first_name},{self.last_name}'

#     def has_perm(self,perm,obj=None):
#         return True
        
#     def has_module_perm(self,app_label):
#         return True