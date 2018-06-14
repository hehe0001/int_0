# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http.response import HttpResponse
from django.shortcuts import render_to_response
import json
# Create your views here.
def Login1(request):
    if request.method =='GET':
        result = {}
        username = request.GET.get('username')
        tele = request.GET.get('telenumber')
        data = request.GET.get('password')
        result['user'] = username
        result['tel'] = tele
        result['data'] = data
        result = json.dumps(result)
        return HttpResponse(username)
    else:
        return render_to_response('loginn1.html')