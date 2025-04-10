# budgeting/models.py
from django.db import models
from categories.models import Category  # Assuming you have a Category model

class Budget(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    period_type = models.CharField(max_length=20, choices=[('Monthly', 'Monthly'), ('Weekly', 'Weekly')])
    start_date = models.DateField()
    end_date = models.DateField()
    is_recurring = models.BooleanField(default=False)
    freeze_on_exceed = models.BooleanField(default=False)
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)  # Assuming you have a User model