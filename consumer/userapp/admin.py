from django.contrib import admin
from .models import *


# Register your models here.
# @admin.register(Manufacturer)
# class ManufacturerAdmin(admin.ModelAdmin):
#     list_display = ('name','licensePic')

@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    search_fields = ['name','code']


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


# class MyAdminSite(admin.AdminSite):
#     site_header = '服药管理系统'
#     index_template = "dataAdmin/index.html"
#     NAME="data_admin"
#     logout_template = "dataAdmin/auth/logout.html"
#     login_template = "dataAdmin/auth/login.html"
#     password_change_template = "dataAdmin/auth/custom/password_change_form.html"
#     password_change_done_template = "dataAdmin/auth/custom/password_change_done.html"
#     def __init__(self):
#         super().__init__(MyAdminSite.NAME)
#     class Meta:
#         pass
# myAdmin=MyAdminSite()