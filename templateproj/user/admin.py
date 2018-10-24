from django.contrib import admin
from django.utils.safestring import mark_safe
from django import  forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group
from user.models import *



@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'code')
    search_fields = ('name', )


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='密码',widget=forms.PasswordInput)
    password2 = forms.CharField(label='确认密码',widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('username','name','department','role','is_admin')

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Password do not match!')
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password2'])
        if commit:
            user.save()
        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = MyUser
        fields = ('username','name','department','role','is_admin')

@admin.register(MyUser)
class MyUserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('username','name', 'role')
    list_filter = ('is_admin',)
    # fieldsets = (
    #     (None, {'fields':('username', 'password')}),
    #     ('Personal Info',{'fields':('name',)}),
    #     ('Permisssions',{'fields':('is_admin',)}),
    # )
    search_fields = ('name','username')
    filter_horizontal = ('department',)
    ordering = ('name',)
    fieldsets = None
    fields = ('username','name','department','role','is_admin')

admin.site.unregister(Group)