from django.db import models
from django.contrib import admin
class Car1(models.Model):
    brand_names=models.CharField(max_length=20)
    car_name=models.CharField(max_length=10)
    enginenum=models.IntegerField()
    release_date=models.DateField()

class Car1Admin(admin.ModelAdmin):
    list_display=('brand_names', 'car_name', 'enginenum', 'release_date')


    
    

# Create your models here.
