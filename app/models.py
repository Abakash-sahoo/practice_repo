from django.db import models

# Create your models here.
class Stu(models.Model):
    sroll=models.IntegerField(primary_key=True)
    sname=models.CharField(max_length=50)
    
