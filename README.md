# Ex02 Django ORM Web Application
## Date: 21-11-2025

## AIM
To develop a Django application to store and retrieve data from a Car Inventory Database using Object Relational Mapping(ORM).

## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 5 Car 

## PROGRAM
```
from django.db import models
from django.contrib import admin
class Car1(models.Model):
    brand_names=models.CharField(max_length=20)
    car_name=models.CharField(max_length=10)
    enginenum=models.IntegerField()
    release_date=models.DateField()

class Car1Admin(admin.ModelAdmin):
    list_display=('brand_names', 'car_name', 'enginenum', 'release_date')

admin.py
from django.contrib import admin
from.models import Car1,Car1Admin
admin.site.register(Car1,Car1Admin)
```
![alt text](<Screenshot 2025-11-21 103805.png>) ![alt text](<Screenshot 2025-11-21 110921.png>)
## OUTPUT
Include your output




## RESULT
Thus the program for creating car inventory database database using ORM hass been executed successfully
