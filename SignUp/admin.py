# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import SignMessage
# Register your models here.

class SignAdmin(admin.ModelAdmin):
    list_display = ('name', 'major', 'phone_num', 'email', 'qq', 'first_choice',
                    'second_choice', 'pub_date')
    search_fields = ('name', )
    list_filter = ('major', 'first_choice')
admin.site.register(SignMessage, SignAdmin)
