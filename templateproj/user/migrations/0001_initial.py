# Generated by Django 2.1 on 2018-10-24 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, unique=True, verbose_name='登录名')),
                ('name', models.CharField(max_length=100, verbose_name='姓名')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('role', models.IntegerField(choices=[(3, '主任'), (2, '采购专员'), (1, '库房管理员'), (0, '普通用户')], default=0, verbose_name='用户角色')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='科室名称')),
                ('code', models.CharField(max_length=20, verbose_name='科室编码')),
            ],
        ),
        migrations.AddField(
            model_name='myuser',
            name='department',
            field=models.ManyToManyField(to='user.Department', verbose_name='所属科室'),
        ),
    ]
