from django.db import models

# Create your models here.

class Msg(models.Model):
    name=models.CharField(max_length=40)
    email=models.CharField(max_length=40)
    mobile=models.BigIntegerField()
    msg=models.CharField(max_length=500)
    
# python manage.py makemigrations   - It will create sql queries

# python manage.py migrate  - execute those queries created by first comaand
