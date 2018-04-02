# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Home(models.Model):
    Title = models.CharField(max_length=300)
    SubTitle = models.CharField(max_length=300)
    ImageUrl = models.CharField(max_length=300)

    def __str__(self):
        return self.Title


class Service(models.Model):
    text1 = models.CharField(max_length=300)
    text2 = models.CharField(max_length=300)

    def __str__(self):
        return self.text1


class Recruit(models.Model):
    text1 = models.CharField(max_length=300)
    text2 = models.CharField(max_length=300)

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=300)


class Contact(models.Model):
    text1 = models.CharField(max_length=300)
    text2 = models.CharField(max_length=300)

    name = models.CharField(max_length=300)
    email = models.EmailField(max_length=300)
    phone = models.CharField(max_length=300)
    message = models.CharField(max_length=300)
