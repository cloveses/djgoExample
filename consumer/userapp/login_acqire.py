import re
from django.shortcuts import HttpResponseRedirect


NOT_LOGIN_URL = ['login','logout']
LOGIN_URL = '/userapp/login/'


class PubAuthMiddleWare:

    def process_request(self, request):
        # url_path = request.path
        # exclued_path = [re.compile(item) for item in NOT_LOGIN_URL]
        # for each in exclued_path:
        #     if re.match(each, url_path):
        #         return
        from .models import User
        # if request.user.is_authenticated:
        #     return HttpResponseRedirect(LOGIN_URL)
        # else:
        #     return
        pass