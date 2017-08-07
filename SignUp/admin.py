# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SignMessage
# Register your models here.

class SignAdmin(admin.ModelAdmin):
    list_display = ('name', 'major', 'phone_num', 'email', 'qq', 'first_choice', 'second_choice', 'recognize', 'introduction')
    search_fields = ('name', )

admin.site.register(SignMessage, SignAdmin)
