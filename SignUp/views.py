# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from SignUp import forms, models
from django.shortcuts import render

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        if form.is_valid():
            message = True
#从表单获取填写的信息
            name = request.POST.get('name')
            major = request.POST.get('major')
            phone_num = request.POST.get('phone_num')
            email = request.POST.get('email')
            qq = request.POST.get('qq')
            first_choice = request.POST.get('first_choice')
            second_choice = request.POST.get('second_choice')
            introduction = request.POST.get('introduction')
            recognize = request.POST.get('recognize')
#录入数据库
            models.SignMessage.objects.create(name=name, major=major, phone_num=phone_num,
                                              email=email, qq=qq, first_choice=first_choice,
                                              second_choice=second_choice, introduction=introduction,
                                              recognize=recognize
                                              )
    form = forms.ContactForm()
    return render(request, 'index.html', locals())

def not_found(request):
    return render(request, '404.html')
