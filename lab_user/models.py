from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):

    def create_user(self, username=None, password=None, **extra_fields):
        if not username or not password:
            raise ValueError('Please fill the fields.')
    
        user = self.model(username,**extra_fields)
        user.set_password(password)
        user.save()
        
        return user

    def create_superuser(self, username, password=None, **extra_fields):
        user = self.create_user(
            username=username,
            password=password,
            **extra_fields
        )
        user.isAdmin = True
        user.profile = '1'
        user.save()
        
        return user


class UserCustom(AbstractBaseUser):

    username = models.CharField(max_length=100, unique=True)
    email = models.CharField(max_length=100, unique=True)
    name = models.CharField('Name', max_length=100, blank=True)
    last_name = models.CharField('Last name', max_length=100, blank=True)
    isActive = models.BooleanField(default=True)
    isAdmin = models.BooleanField(default=False)
    objects = UserManager()
    PROFILES = [
        ('1', 'administrador'),
        ('2', 'operador'),
        ('3', 'inspector'),
        ('4', 'cliente')
    ]
    profile = models.CharField(max_length=1, choices=PROFILES)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name','last_name']

    def __str__(self):
        return f'{self.username}'

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.isAdmin
