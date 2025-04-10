# budgeting/views.py
from django.shortcuts import render, redirect
from .forms import BudgetForm
from .models import Budget 
from categories.models import Category 
from users.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Sum
from transactions.models import Expense



def create_budget(request):
    user_id = request.session.get("user_id")

    if not user_id:
        return redirect('/login/')  # no session user → redirect

    try:
        user = User.objects.get(user_id=user_id)
    except User.DoesNotExist:
        return redirect('/login/')  # invalid user → redirect

    if request.method == "POST":
        amount = request.POST.get('amount')
        period_type = request.POST.get('period_type')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        is_recurring = 'is_recurring' in request.POST
        freeze_on_exceed = 'freeze_on_exceed' in request.POST
        category_id = request.POST.get('category')

        try:
            category = Category.objects.get(id=category_id)
        except Category.DoesNotExist:
            messages.error(request, "Invalid category selected.")
            return redirect('/create-budget/')

        # ✅ now user is guaranteed to exist here
        Budget.objects.create(
            user=user,
            category=category,
            amount=amount,
            period_type=period_type,
            start_date=start_date,
            end_date=end_date,
            is_recurring=is_recurring,
            freeze_on_exceed=freeze_on_exceed
        )

        messages.success(request, "Budget created successfully!")
        return redirect('/display-budget/')

    # ✅ GET request path — just load the form
    categories = Category.objects.all()
    return render(request, 'create_budget.html', {
        'categories': categories
    })

def display_budget(request):
    user_id = request.session.get('user_id')
    if not user_id:
        # Handle unauthenticated users
        return redirect('login')  # or wherever appropriate

    user = User.objects.get(user_id=user_id)
    
    budgets = Budget.objects.filter(user=user)
    
    for budget in budgets:
        total_spent = Expense.objects.filter(
            user=user,
            Category=budget.category,
            date__range=[budget.start_date, budget.end_date]
        ).aggregate(total=Sum('amount'))['total'] or 0

        budget.total_spent = total_spent
        budget.percentage_spent = (total_spent / budget.amount * 100) if budget.amount else 0

        remaining_budget = budget.amount - total_spent
    return render(request, 'display_budget.html', {'budgets': budgets})