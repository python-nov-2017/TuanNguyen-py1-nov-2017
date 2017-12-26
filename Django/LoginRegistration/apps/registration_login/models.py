# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 2:
            errors["first_name"] = "First name has to have at least 2 characters."
        if not postData['first_name'].isalpha():
            errors['first_name'] = "First name cannot have any number."
        if len(postData['first_name']) is 0:
            errors["first_name"] = "First name is required."

         
        if len(postData['last_name']) < 2:
            errors["last_name"] = "Last name has to have at least 2 characters."
        if not postData['last_name'].isalpha():
            errors['last_name'] = "Last name cannot have any number."            
        if len(postData['last_name']) is 0:
            errors["last_name"] = "Last name is required."   

        if not EMAIL_REGEX.match(postData['email']):
            errors["email"] = "Invalid email format"
        if len(postData['email']) is 0:
            errors["email"] = "Email is required."            
        if len(User.objects.filter(email=postData['email'])):
            errors["email"] = "Email is already registered."
        if postData['pw'] != postData['pw_confirm']:
            errors['pw'] = "Password confirmation must match."
        if len(postData['pw']) < 8:
            errors["pw"] = "Password has to have at least 8 characters."             
        if len(postData['pw']) is 0:
            errors["pw"] = "Password is required."            
        
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __repr__(self):
        return "<User Object: {} {}>".format(self.first_name, self.last_name)
    