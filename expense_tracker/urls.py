"""
URL configuration for expense_tracker project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from . import views
from transactions import views as transaction_views
from categories import views as category_views
from budgeting import views as budgeting_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.login),
    path('register/',views.reg),
    path('login/',views.login),
    path('dashboard/',views.dash ),
    path('logout/',views.logout),
    path("add-income/",transaction_views.add_income, name="add_income"),
    path("add-expense/",transaction_views.add_expense, name="add_expense"),
    path("add-category/",category_views.add_category, name="add_category"),
    path("add-category-ajax/",category_views.add_category_ajax, name="add_category_ajax"),
    path('display-income/', transaction_views.display_income, name='display_income'),
    path('display-expense/', transaction_views.display_expense, name='display_expense'),
    path('display-budget/', budgeting_views.display_budget, name='display_budget'),
    path('create-budget/', budgeting_views.create_budget, name='create_budget'),


]

from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
