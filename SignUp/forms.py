# -*- coding: utf-8 -*-
from django import forms

class ContactForm(forms.Form):
    MAJOR_CHOICE = [
        [u'网络工程', u'网络工程'],
        [u'信息安全', u'信息安全'],
        [u'计算科学与技术', u'计算机科学与技术'],
        [u'物联网工程', u'物联网工程'],
        [u'软件工程', u'软件工程']
    ]
    WISH_CHOICE = [
        [u'网络部', u'网络部'],
        [u'创业部', u'创业部'],
        [u'竞赛部', u'竞赛部'],
        [u'社团部', u'社团部']
    ]

    name = forms.CharField(max_length=200, label=u'姓名', widget=forms.TextInput(attrs={'placeholder': u'姓名'}))
    major = forms.ChoiceField(choices=MAJOR_CHOICE, label=u'专业')
    phone_num = forms.CharField(max_length=200, label=u'电话', widget=forms.TextInput(attrs={'placeholder': u'电话号码'}))
    email = forms.EmailField(label=u'邮箱', widget=forms.EmailInput(attrs={'placeholder': u'常用邮箱地址'}))
    qq = forms.CharField(max_length=200, label=u'QQ', widget=forms.TextInput(attrs={'placeholder': u'QQ'}))
    first_choice = forms.ChoiceField(choices=WISH_CHOICE, label=u'第一志愿')
    second_choice = forms.ChoiceField(choices=WISH_CHOICE, label=u'第二志愿')
    recognize = forms.CharField(label=u'对科协的认识', widget=forms.Textarea(attrs={'placeholder': u'对科协的认识', 'class': 'desciption'}))
    introduction = forms.CharField(label=u'自我介绍', widget=forms.Textarea(attrs={'placeholder': u'自我介绍', 'class': 'desciption'}))