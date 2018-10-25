from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.http import require_http_methods
from userapp import models
from django.forms import ModelForm
from django.http import JsonResponse
from django.views import generic
from django.urls import reverse
import datetime

# Create your views here.

