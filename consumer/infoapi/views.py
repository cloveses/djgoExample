from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from userapp import models
from django.forms import ModelForm
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse
import datetime

# Create your views here.

class ProductForm(ModelForm):
    class Meta:
        model = models.Product
        # fields = '__all__'
        exclude = ['sign_flag',]

class PrOrAgForm(ModelForm):
    class Meta:
        model = models.ProducerOrAgency
        fields = '__all__'

class EnterHostpitalForm(ModelForm):
    class Meta:
        model = models.EnterHostpital
        exclude = ['sign_user', 'sign_flag', 'sign_time']

# 上传产品API
@require_http_methods(['POST','GET'])
def recv_product(request):
    if request.method == 'GET':
        form = ProductForm()
        return render(request, 'upload.html', {'form':form, 'action': 'upload_product'})
    form = ProductForm(request.POST or None, request.FILES)
    print(form.errors)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 0})
    return JsonResponse({'status': 1})


# 上传生产商、销售商、代理商API
@require_http_methods(['POST','GET'])
def recv_prdoragc(request):
    if request.method == 'GET':
        form = PrOrAgForm()
        return render(request, 'upload.html', {'form':form, 'action': 'upload_prdoragc'})
    else:
        form = EnterHostpitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 0})
        else:
            return JsonResponse({'status': 1})


# 产品列表页面
class ProductList(generic.ListView):
    template_name = 'product.html'
    context_object_name = 'datas'
    def get_queryset(self):
        return models.Product.objects.all()

# 填写入院单（通过产品列表页面进入）
def add_enter_hospital(request, id):
    if request.method == 'GET':
        product = models.Product.objects.get(pk=id)
        form = EnterHostpitalForm()
        return render(request, 'add_enter_hospital.html', {'product':product, 'form': form})
    else:
        form = EnterHostpitalForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('product_list'))

# 审批入院单
def sign_enter_hospital(request, id=0):
    if request.method == 'GET':
        enter_hospitals = models.EnterHostpital.objects.filter(sign_flag=False)
        return render(request, 'sign_enter_hostpital.html', {'datas': enter_hospitals})
    else:  #POST请求由AJAX完成
        if id:
            enter_hospital = models.EnterHostpital.objects.get(pk=id)
            enter_hospital.sign_time = datetime.datetime.now()
            enter_hospital.sign_name = request.POST['name']
            enter_hospital.sign_flag = True
            return JsonResponse({'status': 0})
        else:
            return JsonResponse({'status': 1})

# 请领
class RequestOrderForm(ModelForm):
    class Meta:
        model = models.RequestOrder
        exclude = ['status',]

def add_requestorder(request):
    if request.method == 'GET':
        form = RequestOrderForm()
        return render(request, 'add_requestorder.html', {'form': form})
    else:
        form = RequestOrderForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(reverse('add_requestorder'))
