from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True, max_length=100)
    password = models.CharField(max_length=255) 
    currency = models.CharField(max_length=10, default='INR')
    registration_date = models.DateTimeField(auto_now_add=True)


    
    

