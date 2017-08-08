# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
# Create your models here.

class SignMessage(models.Model):
    MAJOR_CHOICE = (
        ('网络工程', '网络工程'),
        ('信息安全', '信息安全'),
        ('计算科学与技术', '计算机科学与技术'),
        ('物联网工程', '物联网工程'),
        ('软件工程', '软件工程'),
    )
    WISH_CHOICE = (
        ('网络部', '网络部'),
        ('创业部', '创业部'),
        ('竞赛部', '竞赛部'),
        ('社团部', '社团部')
    )

    name = models.CharField(max_length=200, verbose_name='姓名')
    major = models.CharField(max_length=200, choices=MAJOR_CHOICE, verbose_name='专业')
    phone_num = models.CharField(max_length=200, verbose_name='电话')
    email = models.EmailField(verbose_name='邮箱')
    qq = models.CharField(max_length=200, verbose_name='QQ')
    first_choice = models.CharField(max_length=200, choices=WISH_CHOICE, verbose_name='第一志愿')
    second_choice = models.CharField(max_length=200, choices=WISH_CHOICE, verbose_name='第二志愿')
    recognize = models.TextField(verbose_name='对科协的认识')
    introduction = models.TextField(verbose_name='自我介绍')
    pub_date = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-pub_date', )
        verbose_name = u'报名信息'
        verbose_name_plural = u'报名信息'

    def __unicode__(self):
        return self.name
