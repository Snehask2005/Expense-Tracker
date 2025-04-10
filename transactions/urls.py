from django.urls import path
from .views import IncomeListCreateView, IncomeDetailView, ExpenseListCreateView, ExpenseDetailView

urlpatterns = [
    path('income/', IncomeListCreateView.as_view(), name='income-list-create'),
    path('income/<int:pk>/', IncomeDetailView.as_view(), name='income-detail'),
    path('expense/', ExpenseListCreateView.as_view(), name='expense-list-create'),
    path('expense/<int:pk>/', ExpenseDetailView.as_view(), name='expense-detail'),
]
