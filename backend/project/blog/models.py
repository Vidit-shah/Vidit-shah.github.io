from django.db import models

# Create your models here.
class Vedio(models.Model):
    vedio_id = models.AutoField
    vedio_link = models.CharField(max_length=100)
    vedio_name = models.CharField(max_length=100)
    dec = models.CharField(max_length=500)
