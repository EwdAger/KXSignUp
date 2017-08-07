# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.template.loader import get_template
from django.shortcuts import render
from SignUp import forms
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.

def index(request):
    form = forms.ConteactForm()
    template = get_template('index.html')
    request_context = RequestContext(request)
    request_context.push(locals())
    html = template.render(request_context)

    return HttpResponse(html)

def Posy(request):
    return render(request, 'index.html')