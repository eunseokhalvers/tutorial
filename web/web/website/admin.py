# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import  Home, Service, Recruit, Contact

admin.site.register(Home)
admin.site.register(Service)
admin.site.register(Contact)
admin.site.register(Recruit)