from django.db import models
from django.urls.base import set_urlconf

# Create your models here.

class Equipment(models.Model):
    equipment_id=models.AutoField(primary_key=True,verbose_name='Equipemt ID')
    equipment_name=models.CharField(max_length=100,verbose_name='Equipment Name')
    primary_desc=models.CharField(max_length=1000,verbose_name='Primary Description')
    rental=models.DecimalField(max_digits=5,decimal_places=3,verbose_name="Rate per hour",help_text="₹/Hour")
    secondary_desc=models.TextField(verbose_name="Secondary Description")
    primary_img=models.ImageField(verbose_name="Primary Image")
    # secondary_img=models.ForeignKey(Secondary_Image,on_delete=models.CASCADE)

class Secondary_Image(models.Model):
    image_id=models.AutoField(primary_key=True,verbose_name='Image ID')
    equipment = models.ForeignKey(Equipment,on_delete=models.CASCADE)
    secondary_img = models.ImageField(verbose_name='Secondary Image')



