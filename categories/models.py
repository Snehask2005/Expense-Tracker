from django.db import models
from users.models import User

# Create your models here.

class Category(models.Model):
    INCOME = 'Income'
    EXPENSE = 'Expense'
    
    CATEGORY_TYPES = [
        (INCOME, 'Income'),
        (EXPENSE, 'Expense'),
    ]

    category_name = models.CharField(max_length=100, unique=True)
    category_type = models.CharField(max_length=100, choices=CATEGORY_TYPES)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.category_name} ({self.category_type})"
