from django.db import models

 
class persons(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    first_name = models.CharField(max_length=255, null=False)
    last_name = models.CharField(max_length=255, null=False)
    middle_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=12, null=False)
    city = models.CharField(max_length=255, null=False)
    address = models.CharField(max_length=255, null=False)
    
    class Meta:
        db_table = 'persons'



class logons(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    person = models.ForeignKey(persons, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=False, unique=True)
    password = models.CharField(max_length=255, null=False)
    
    class Meta:
        db_table = 'logons'




class calls(models.Model):
    id = models.AutoField(primary_key=True, blank=False, null=False)
    person = models.ForeignKey(persons, on_delete=models.CASCADE)
    message = models.TextField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=255, null=False, default='actual')
    
    class Meta:
        db_table = 'calls'