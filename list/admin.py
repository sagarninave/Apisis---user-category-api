# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from list.models import *

admin.site.register(User)
admin.site.register(UserCategory)
admin.site.register(Category)
admin.site.register(SubCategory)
admin.site.register(Item)