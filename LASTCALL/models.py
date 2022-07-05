from django.db import models
from traitlets import default
 
class persons(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
	middle_name = models.CharField(max_length=255)
	phone_number = models.CharField(max_length=12, null=False)
	city = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)



class logons(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    person_id = models.ForeignKey(persons)
    name = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)




class calls(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    person_id = models.ForeignKey(persons)
    message = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, null=False, default='actual')