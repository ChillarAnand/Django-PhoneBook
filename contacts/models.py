from django.db import models

# Create your models here.

class Person(models.Model):
    first_name = models.CharField(max_length=100, db_index=True)
    last_name = models.CharField(max_length=100, default='')
    phone_no = models.CharField(max_length=15)
    address = models.TextField(default='')
    email = models.EmailField(default='') 


class ExtraDetail(models.Model):
    person = models.OneToOneField(Person, null=True)
    website = models.URLField(max_length=100)
    notes = models.TextField(default='')
    birthday = models.DateField(default='', null=True)
    relationship = models.CharField(max_length=100, default='')

