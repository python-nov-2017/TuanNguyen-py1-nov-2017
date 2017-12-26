# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.

class BlogManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email"
        # if len(postData['name']) < 5:
        #     errors["name"] = "Blog name should be more than 5 characters"
        # if len(postData['desc']) < 10:
        #     errors["desc"] = "Blog desc should be more than 10 characters"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    update_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()
    def __repr__(self):
        return "<User object: name: {} {} >".format(self.first_name, self.last_name)