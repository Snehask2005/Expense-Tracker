from django.db import models
from users.models import User
from categories.models import Category



# Create your models here.

class Income(models.Model):
    income_id = models.AutoField(primary_key= True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    source = models.CharField(max_length=100)
    description = models.TextField(blank = True, null = True)


def __str__(self):
    return f"{self.source} - ₹{self.amount} on {self.date}"


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    Category = models.ForeignKey(Category, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    recurring_flag = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

def __str__(self):
    return f"{self.category} - ₹{self.amount} on {self.date}"
