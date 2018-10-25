# Generated by Django 2.0.7 on 2018-10-15 02:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0002_auto_20181015_0812'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_datetime', models.DateTimeField(auto_now=True, verbose_name='请领时间')),
                ('request_amount', models.FloatField(verbose_name='数量')),
                ('status', models.IntegerField(choices=[(0, '请领'), (1, '缺货'), (2, '缺货补货中'), (3, '待出库'), (4, '已出库')], default=0, verbose_name='状态')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Department', verbose_name='请领科室')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='请领产品')),
                ('request_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User', verbose_name='请领人')),
            ],
        ),
        migrations.RemoveField(
            model_name='requestoder',
            name='department',
        ),
        migrations.RemoveField(
            model_name='requestoder',
            name='product',
        ),
        migrations.RemoveField(
            model_name='requestoder',
            name='request_user',
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.ProducerOrAgency', verbose_name='生产商'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='产品'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='userapp.ProducerOrAgency', verbose_name='销售商或一级代理'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='seller_auth',
            field=models.ImageField(null=True, upload_to='', verbose_name='授权书'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='seller_valid',
            field=models.DateField(null=True, verbose_name='有效期限'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='sign_time',
            field=models.DateTimeField(null=True, verbose_name='审批时间'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='sign_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User', verbose_name='审批人'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='two_agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency', to='userapp.ProducerOrAgency', verbose_name='二级代理'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='two_agency_auth',
            field=models.ImageField(null=True, upload_to='', verbose_name='授权书'),
        ),
        migrations.AlterField(
            model_name='enterhostpital',
            name='two_agency_valid',
            field=models.DateField(null=True, verbose_name='有效期限'),
        ),
        migrations.DeleteModel(
            name='RequestOder',
        ),
    ]
