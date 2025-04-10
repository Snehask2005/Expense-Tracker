from rest_framework import serializers
from .models import Budget

class BudgetSerializer(serializers.ModelSerializer):
    total_spent = serializers.SerializerMethodField()
    remaining = serializers.SerializerMethodField()
    is_exceeded = serializers.SerializerMethodField()
    is_near_limit = serializers.SerializerMethodField()

    class Meta:
        model = Budget
        fields = ['id', 'user', 'category', 'amount', 'period_type', 'start_date', 'end_date',
                  'is_recurring', 'freeze_on_exceed', 'total_spent', 'remaining', 'is_exceeded', 'is_near_limit']
        read_only_fields = ['user', 'total_spent', 'remaining', 'is_exceeded', 'is_near_limit']

    def get_total_spent(self, obj):
        return obj.get_total_spent()

    def get_remaining(self, obj):
        return obj.get_remaining_budget()

    def get_is_exceeded(self, obj):
        return obj.is_exceeded()

    def get_is_near_limit(self, obj):
        return obj.is_near_limit()