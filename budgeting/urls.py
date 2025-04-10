# budgeting/urls.py
from django.urls import path
from .views import create_budget

urlpatterns = [
    path('budgets/create/', create_budget, name='create_budget'),
]
