from django.shortcuts import render, redirect
from categories.models import Category

# Create your views here.
def add_category(request):
    user_id = request.session.get("user_id")
    if not user_id:
        return redirect('/login/')

    if request.method == "POST":
        category_name = request.POST['category_name']
        category_type = request.POST['category_type']

        # Check if category already exists for the user or globally
        exists = Category.objects.filter(category_name__iexact=category_name, user_id__in=[None, user_id]).exists()
        if not exists:
            Category.objects.create(
                category_name=category_name,
                category_type=category_type,
                user_id=user_id
            )
        return redirect('/dashboard/')  # or redirect wherever you want

    return render(request, 'add_category.html')

from django.http import JsonResponse


def add_category_ajax(request):
    if request.method == "POST":
        name = request.POST.get("category_name")
        if name:
            cat = Category.objects.create(category_name=name)
            return JsonResponse({"success": True, "category_id": cat.category_id, "category_name": cat.category_name})
    return JsonResponse({"success": False})

