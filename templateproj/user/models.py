from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.contrib.auth import get_user_model
# import settings

# Create your models here.


class MyUserMgr(BaseUserManager):

    def create_user(self, username, name, password):
        user = self.model(username=username, name=name)
        if not password:
            raise ValueError('User must have password!')
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, name, password):
        user = self.model(username=username, name=name, password=password)
        # if not password:
        #     raise ValueError('User must have password!')
        # user.set_password(password)
        user.is_admin = True
        user.set_password(password)
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True, verbose_name='登录名')
    name = models.CharField(max_length=100, verbose_name='姓名')
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    department = models.ManyToManyField('Department', verbose_name='所属科室')
    choices = ((3, '主任'),(2, '采购专员'),(1, '库房管理员'),(0,'普通用户'))
    role = models.IntegerField(choices=choices,default=0, verbose_name='用户角色')

    objects = MyUserMgr()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['name',]

    def get_full_name(self):
        return "%s(%s)" % (self.username,self.name)

    def get_short_name(self):
        return  self.name

    def __str__(self):
        return self.get_full_name()

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return  self.is_admin

class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='科室名称')
    code = models.CharField(max_length=20, verbose_name='科室编码')

    def __str__(self):
        return self.name