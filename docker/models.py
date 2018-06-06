from django.db import models

# Create your models here.
class hosts(models.Model):
    host=models.CharField(max_length=50)
    count=models.IntegerField()