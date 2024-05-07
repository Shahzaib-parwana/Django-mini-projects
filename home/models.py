from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Students(models.Model):
    user = models.ForeignKey(User,on_delete=models.SET_NULL,null=True ,blank=True)
    name = models.CharField(max_length=100)
    father_name = models.CharField(max_length=100)
    department =models.TextField(max_length=100)
    semister = models.CharField(max_length=10)
    roll_no = models.CharField(max_length=8)
    image = models.ImageField(upload_to='add',default='templates/pic1.jpg')
