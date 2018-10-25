"""consumer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from . import views

urlpatterns = [
    # path('', views.test),
    # path('login/', views.login, name= 'login'),
    # path('usermgr/', views.UserMgr.as_view(), name='usermgr'),
    # path('adduser/', views.add_user, name= 'adduser'),
    # path('deluser/<int:id>/', views.del_user, name= 'deluser')
    path('upload_product/', views.recv_product, name= 'upload_product'),
    path('upload_prdoragc/', views.recv_prdoragc, name= 'upload_prdoragc'),
    path('product_list/', views.ProductList.as_view()),
    path('add_enter_hospital/<int:id>', views.add_enter_hospital, name = 'add_enter_hospital'),
    path('sign_enter_hospital/<int:id>', views.sign_enter_hospital, name= 'sign_enter_hospital'),
    path('add_requestorder', views.add_requestorder, name= 'add_requestorder')
]
