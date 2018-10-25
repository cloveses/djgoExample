# Generated by Django 2.0.7 on 2018-10-15 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='科室名称')),
                ('code', models.CharField(max_length=20, verbose_name='科室编码')),
            ],
        ),
        migrations.CreateModel(
            name='EnterHostpital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_auth', models.ImageField(null=True, upload_to='')),
                ('seller_valid', models.DateField(null=True)),
                ('two_agency_auth', models.ImageField(null=True, upload_to='')),
                ('two_agency_valid', models.DateField(null=True)),
                ('sign_time', models.DateTimeField(auto_now=True)),
                ('sign_flag', models.BooleanField(default=False, verbose_name='审批标志')),
            ],
        ),
        migrations.CreateModel(
            name='IncomingInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('in_datetime', models.DateTimeField(auto_now=True, verbose_name='入库日期')),
                ('way', models.IntegerField(choices=[(0, '按单入库'), (1, '赠送入库'), (2, '其他入库')], verbose_name='入库方式')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(verbose_name='发票金额')),
                ('sign_datetime', models.DateTimeField(verbose_name='开票日期')),
            ],
        ),
        migrations.CreateModel(
            name='OutInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('out_datetime', models.DateTimeField(auto_now=True, verbose_name='出库时间')),
                ('reciever', models.CharField(max_length=50, verbose_name='领取人')),
                ('way', models.IntegerField(choices=[(0, '请领单出库'), (1, '其他出库')], verbose_name='出库方式')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Department', verbose_name='领取科室')),
            ],
        ),
        migrations.CreateModel(
            name='ProducerOrAgency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='企业名称')),
                ('duty_id', models.CharField(max_length=20, verbose_name='企业税号')),
                ('addr', models.CharField(max_length=100, verbose_name='企业地址')),
                ('deposit_bank', models.CharField(max_length=20, verbose_name='开户银行')),
                ('account_id', models.CharField(max_length=20, verbose_name='开户账号')),
                ('telephone', models.CharField(max_length=18, verbose_name='联系电话')),
                ('licence', models.ImageField(upload_to='', verbose_name='营业执照')),
                ('old_name', models.CharField(max_length=100, verbose_name='曾用名')),
                ('precursor', models.CharField(max_length=100, verbose_name='企业前身')),
                ('vote_limit', models.IntegerField(verbose_name='开票限额')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='产品名称')),
                ('common_name', models.CharField(max_length=20, verbose_name='通用名')),
                ('brand', models.CharField(max_length=20, verbose_name='品牌名称')),
                ('reg_number', models.CharField(max_length=100, unique=True, verbose_name='注册证号')),
                ('certification', models.ImageField(upload_to='', verbose_name='注册证')),
                ('specification', models.CharField(max_length=50, verbose_name='规格')),
                ('unit', models.IntegerField(choices=[(0, '袋'), (1, '盒')], verbose_name='单位')),
                ('sign_flag', models.BooleanField(default=False, verbose_name='审批标志')),
            ],
        ),
        migrations.CreateModel(
            name='RequestOder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('request_datetime', models.DateTimeField(auto_now=True, verbose_name='请领时间')),
                ('request_amount', models.FloatField(verbose_name='数量')),
                ('status', models.IntegerField(choices=[(0, '请领'), (1, '缺货'), (2, '缺货补货中'), (3, '待出库'), (4, '已出库')], verbose_name='状态')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Department', verbose_name='请领科室')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='请领产品')),
            ],
        ),
        migrations.CreateModel(
            name='SellerOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_datetime', models.DateTimeField(auto_now=True, verbose_name='订单时间')),
                ('unit_price', models.FloatField(verbose_name='单价')),
                ('amount', models.FloatField(verbose_name='数量')),
                ('total_price', models.FloatField(verbose_name='总价')),
                ('status', models.IntegerField(choices=[(0, '未开'), (1, '已生成'), (2, '已开')], verbose_name='开票状态')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='产品')),
                ('sign_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.InvoiceInfo', verbose_name='发票编号')),
            ],
        ),
        migrations.CreateModel(
            name='StockInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quality', models.FloatField(verbose_name='库存数量')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='产品')),
            ],
        ),
        migrations.CreateModel(
            name='StoreRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='库房名称')),
                ('addr', models.CharField(max_length=50, verbose_name='库房地址')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='用户名称')),
                ('passwd', models.CharField(max_length=128, verbose_name='密码')),
                ('token', models.CharField(default='', max_length=128)),
                ('role', models.IntegerField(choices=[(2, '主任'), (1, '采购专员'), (0, '库房管理员')], default=0, verbose_name='用户角色')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Department', verbose_name='所属科室')),
            ],
        ),
        migrations.CreateModel(
            name='WarningInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_limit', models.IntegerField(verbose_name='预警下限')),
                ('max_limit', models.IntegerField(verbose_name='预警上限')),
                ('total_limit', models.FloatField(verbose_name='采购数额预警总额')),
                ('month_limit', models.IntegerField(verbose_name='月度采购数额预警')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='产品')),
            ],
        ),
        migrations.AddField(
            model_name='storeroom',
            name='clerk',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userapp.User', verbose_name='库房管理员'),
        ),
        migrations.AddField(
            model_name='stockinfo',
            name='storeroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.StoreRoom', verbose_name='库房'),
        ),
        migrations.AddField(
            model_name='requestoder',
            name='request_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User', verbose_name='请领人'),
        ),
        migrations.AddField(
            model_name='produceroragency',
            name='product',
            field=models.ManyToManyField(to='userapp.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='outinfo',
            name='out_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User', verbose_name='出库人'),
        ),
        migrations.AddField(
            model_name='outinfo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='outinfo',
            name='storeroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.StoreRoom', verbose_name='库房'),
        ),
        migrations.AddField(
            model_name='invoiceinfo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='incominginfo',
            name='in_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User', verbose_name='入库人员'),
        ),
        migrations.AddField(
            model_name='incominginfo',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product', verbose_name='产品'),
        ),
        migrations.AddField(
            model_name='incominginfo',
            name='storeroom',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.StoreRoom', verbose_name='入库库房'),
        ),
        migrations.AddField(
            model_name='enterhostpital',
            name='producer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.ProducerOrAgency'),
        ),
        migrations.AddField(
            model_name='enterhostpital',
            name='product',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='userapp.Product'),
        ),
        migrations.AddField(
            model_name='enterhostpital',
            name='seller',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='seller', to='userapp.ProducerOrAgency'),
        ),
        migrations.AddField(
            model_name='enterhostpital',
            name='sign_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userapp.User'),
        ),
        migrations.AddField(
            model_name='enterhostpital',
            name='two_agency',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agency', to='userapp.ProducerOrAgency'),
        ),
    ]