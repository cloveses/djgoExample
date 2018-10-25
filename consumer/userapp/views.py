import hashlib
import datetime
from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.http import JsonResponse
from django.forms import ModelForm
from userapp.models import (User,)
from django.views import generic
from django.urls import reverse
# Create your views here.


class LogForm(ModelForm):
    class Meta:
        model = User
        fields = ['name','passwd']


def make_passwd(s,salt=''):
    res = hashlib.sha3_512(s.encode('utf-8')).hexdigest()
    if salt:
        res += salt
        res = hashlib.sha3_512(res.encode('utf-8')).hexdigest()
    return res


def make_token(s):
    t = str(datetime.datetime.now())
    return make_passwd(s+t)


def verify_user(name, passwd):
    u = User.objects.filter(name=name).filter(passwd=passwd).first()
    if u:
        token = make_token(name+passwd)
        u.token = token
        u.save()
        return token
    else:
        return ''


def test(request):
    return HttpResponse('hw ')


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        exclude = ['token',]

    def clean_passwd(self):
        passwd = self.cleaned_data.get('passwd')
        if passwd:
            return make_passwd(passwd,self.cleaned_data.get('name'))
        else:
            return ''


class UserMgr(generic.ListView):
    template_name = 'usermgr.html'
    context_object_name = 'datas'

    def get_queryset(self):
        return User.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = UserForm()
        return context


def add_user(request):
    form = UserForm(request.POST)
    if form.is_valid():
        form.save()
        return JsonResponse({'status': 0})
    else:
        return JsonResponse({'status': 1})


def del_user(request, id):
    User.get(pk=id).delete()
    return HttpResponseRedirect(reverse('usermgr'))


def login(request):
    if request.method == 'GET':
        form = LogForm()
        return render(request, 'login.html', {'form':form})
    else:
        name = request.POST.get('name', None)
        passwd = request.POST.get('passwd', None)
        if name and passwd:
            passwd = make_passwd(passwd,name)
            res = verify_user(name,passwd)
            if res:
                return JsonResponse({'status':0, 'data': {'token':res}})
            else:
                return JsonResponse({'status': 1, 'msg': 'name or password Error!'})
        else:
            return JsonResponse({'status': 1, 'msg': 'Data not Enough!'})