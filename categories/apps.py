from django.apps import AppConfig


class CategoriesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'categories'
    
class ExpensesConfig(AppConfig):  # or your app name
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'expenses'  # change this if your app name is different

    def ready(self):
        from .models import Category
        from django.db.utils import OperationalError
        try:
            defaults = ['Food', 'Transport', 'Groceries', 'Shopping', 'Entertainment', 'Home', 'Health', 'Utilities']
            for name in defaults:
                Category.objects.get_or_create(name=name)
        except OperationalError:
            # Avoid errors on first migration when table may not exist yet
            pass