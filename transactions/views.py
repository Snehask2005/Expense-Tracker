from django.shortcuts import render, redirect
from .models import Income, Expense
from categories.models import Category
from users.models import User
from datetime import datetime
from django.utils import timezone
from django.db.models import Sum
from django.db import models
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import never_cache
from django.shortcuts import get_object_or_404


def add_income(request):
    if request.method == 'POST':
        # Retrieve user_id from session
        user_id = request.session.get('user_id')

        if not user_id:
            return redirect('/login/')  # user is not logged in

        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return redirect('/login/')

        # Get the rest of your form data (example)
        amount = request.POST.get('amount')
        date = request.POST.get('date')
        source = request.POST.get('source')
        description = request.POST.get('description')
        # ... other fields

        income = Income(
            user=user,  
            amount=amount,
            date=datetime.strptime(date, '%Y-%m-%d'),  # assuming date is in YYYY-MM-DD format
            source=source,
            description=description,

            
           
        )
        income.save()
        return redirect('/dashboard/')  # or wherever

    return render(request, 'add_income.html')

def display_income(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect("/login/")

    incomes = Income.objects.filter(user_id=user_id)

    # Total income amount
    total_income = incomes.aggregate(total=Sum('amount'))['total'] or 0

    return render(request, 'display_income.html', {
        'incomes': incomes,
        'total_income': total_income
    })


@never_cache
def add_expense(request):
    user_id = request.session.get("user_id")

    if request.method == "POST":
        amount = request.POST.get("amount")
        date = request.POST.get("date")
        recurring = request.POST.get("recurring_flag", "0")
        description = request.POST.get("description")
        category_id = request.POST.get("category")
        selected_category = get_object_or_404(Category, id=category_id)

        expense = Expense(
            amount=amount,
            date=date,
            recurring_flag=recurring,
            description=description,
            Category_id=category_id,
            user_id=user_id
        )
        expense.save()
        return redirect("/dashboard/")
    

    # Fetch only expense categories
    categories = Category.objects.filter(category_type="expense")
    return render(request, "add_expense.html", {"categories": categories})

def display_expense(request):
        user_id = request.session.get("user_id")
        if not user_id:
            return redirect("/login/")

        expenses = Expense.objects.filter(user_id=user_id)

        # Total expense amount
        total_expense = expenses.aggregate(total=Sum('amount'))['total'] or 0

        return render(request, 'display_expense.html', {
            'expenses': expenses,
            'total_expense': total_expense
        })