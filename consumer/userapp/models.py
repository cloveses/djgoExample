from django.db import models

# Create your models here.


class Department(models.Model):
    name = models.CharField(max_length=50, verbose_name='科室名称')
    code = models.CharField(max_length=20, verbose_name='科室编码')

    def __str__(self):
        return self.name


class User(models.Model):
    name = models.CharField(max_length=30, verbose_name='用户名称')
    passwd = models.CharField(max_length=128, verbose_name='密码')
    token = models.CharField(max_length=128, default='')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='所属科室')
    choices = ((2, '主任'),(1, '采购专员'),(0, '库房管理员'))
    role = models.IntegerField(choices=choices,default=0, verbose_name='用户角色')
    def __str__(self):
        return self.name


class StoreRoom(models.Model):
    name = models.CharField(max_length=30, verbose_name='库房名称')
    addr = models.CharField(max_length=50, verbose_name='库房地址')
    clerk = models.OneToOneField('User', on_delete=models.CASCADE, verbose_name='库房管理员')


class Product(models.Model):
    name = models.CharField(max_length=50, verbose_name='产品名称')
    common_name = models.CharField(max_length=20, verbose_name='通用名')
    brand = models.CharField(max_length=20, verbose_name='品牌名称')
    reg_number = models.CharField(max_length=100, verbose_name='注册证号', unique=True)
    certification = models.ImageField(verbose_name='注册证')
    specification = models.CharField(max_length=50, verbose_name='规格')
    choices = ((0, '袋'),(1, '盒'))
    unit = models.IntegerField(choices=choices, verbose_name='单位')
    sign_flag = models.BooleanField(default=False, verbose_name='审批标志')


class ProducerOrAgency(models.Model):
    name = models.CharField(max_length=100, verbose_name='企业名称')
    duty_id = models.CharField(max_length=20, verbose_name='企业税号')
    addr = models.CharField(max_length=100, verbose_name='企业地址')
    deposit_bank = models.CharField(max_length=20, verbose_name='开户银行')
    account_id = models.CharField(max_length=20, verbose_name='开户账号')
    telephone = models.CharField(max_length=18, verbose_name='联系电话')
    licence = models.ImageField(verbose_name='营业执照')
    old_name = models.CharField(max_length=100, verbose_name='曾用名')
    precursor = models.CharField(max_length=100, verbose_name='企业前身')
    vote_limit = models.IntegerField(verbose_name='开票限额')
    product = models.ManyToManyField('Product', verbose_name='产品')


class StockInfo(models.Model):
    quality = models.FloatField(verbose_name='库存数量')
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='产品')
    storeroom = models.ForeignKey('StoreRoom', on_delete=models.CASCADE, verbose_name='库房')


class IncomingInfo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='产品')
    storeroom = models.ForeignKey('StoreRoom', on_delete=models.CASCADE, verbose_name='入库库房')
    in_datetime = models.DateTimeField(auto_now=True, verbose_name='入库日期')
    in_user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='入库人员')
    ways = ((0, '按单入库'),(1, '赠送入库'),(2, '其他入库'))
    way = models.IntegerField(choices=ways, verbose_name='入库方式')


class OutInfo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='产品')
    storeroom = models.ForeignKey('StoreRoom', on_delete=models.CASCADE, verbose_name='库房')
    out_datetime = models.DateTimeField(auto_now=True, verbose_name='出库时间')
    out_user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='出库人')
    department = models.ForeignKey(Department, on_delete=models.CASCADE, verbose_name='领取科室')
    reciever = models.CharField(max_length=50, verbose_name='领取人')
    ways = ((0, '请领单出库'),(1, '其他出库'))
    way = models.IntegerField(choices=ways, verbose_name='出库方式')


class WarningInfo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='产品')
    min_limit = models.IntegerField(verbose_name='预警下限')
    max_limit = models.IntegerField(verbose_name='预警上限')
    total_limit = models.FloatField(verbose_name='采购数额预警总额')
    month_limit = models.IntegerField(verbose_name='月度采购数额预警')


class InvoiceInfo(models.Model):
    amount = models.FloatField(verbose_name='发票金额')
    sign_datetime = models.DateTimeField(verbose_name='开票日期')
    product = models.ForeignKey('Product',on_delete=models.CASCADE, verbose_name='产品')


class SellerOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='产品')
    order_datetime = models.DateTimeField(auto_now=True, verbose_name='订单时间')
    unit_price = models.FloatField(verbose_name='单价')
    amount = models.FloatField(verbose_name='数量')
    total_price = models.FloatField(verbose_name='总价')
    statuses = ((0,'未开'),(1,'已生成'),(2,'已开'))
    status = models.IntegerField(choices=statuses, verbose_name='开票状态')
    sign_code = models.ForeignKey('InvoiceInfo', on_delete=models.CASCADE, verbose_name='发票编号')


class RequestOrder(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name='请领产品')
    request_datetime = models.DateTimeField(auto_now=True, verbose_name='请领时间')
    request_amount = models.FloatField(verbose_name='数量')
    request_user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='请领人')
    department = models.ForeignKey('Department', on_delete=models.CASCADE, verbose_name='请领科室')
    statuses = ((0, '请领'), (1, '缺货'), (2, '缺货补货中'),(3, '待出库'), (4, '已出库'))
    status = models.IntegerField(choices=statuses, default=0, verbose_name='状态')



class EnterHostpital(models.Model):
    product = models.OneToOneField('Product', on_delete=models.CASCADE, verbose_name='产品')
    producer = models.ForeignKey('ProducerOrAgency', on_delete=models.CASCADE, verbose_name='生产商')
    seller = models.ForeignKey('ProducerOrAgency', null=True, on_delete=models.CASCADE, related_name='seller', verbose_name='销售商或一级代理')
    seller_auth = models.ImageField(null=True, verbose_name='授权书')
    seller_valid = models.DateField(null=True, verbose_name='有效期限')
    two_agency = models.ForeignKey('ProducerOrAgency', null=True, on_delete=models.CASCADE, related_name='agency', verbose_name='二级代理')
    two_agency_auth = models.ImageField(null=True, verbose_name='授权书')
    two_agency_valid = models.DateField(null=True, verbose_name='有效期限')
    sign_time = models.DateTimeField(null=True, verbose_name='审批时间')
    sign_user = models.ForeignKey('User', on_delete=models.CASCADE, verbose_name='审批人')
    sign_flag = models.BooleanField(default=False, verbose_name='审批标志')