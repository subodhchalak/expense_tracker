from rest_framework import serializers
from expense_app.models import (
    ExpenseCategory, ExpenseSubCategory, Person
)

# ---------------------------------------------------------------------------- #
#                         ExpenseSubCategorySerializer                         #
# ---------------------------------------------------------------------------- #

class ExpenseSubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseSubCategory
        fields = (
            'id',
            'sys_id',
            'category',
            'name',
            'short_description',
            'description',
            'status',
            'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id',
            'sys_id',
            'created_at',
            'updated_at'
        )
        
# ---------------------------------------------------------------------------- #
#                           ExpenseCategorySerializer                          #
# ---------------------------------------------------------------------------- #

class ExpenseCategorySerializer(serializers.ModelSerializer):
    expense_sub_category = ExpenseSubCategorySerializer(many=True, read_only=True)
    class Meta:
        model = ExpenseCategory
        fields = (
            'id',
            'sys_id',
            'name',
            'short_description',
            'description',
            'status',
            'expense_sub_category',
            'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id',
            'sys_id',
            'created_at',
            'updated_at'
        )

# ---------------------------------------------------------------------------- #
#                               PersonSerializer                               #
# ---------------------------------------------------------------------------- #

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = (
            'id',
            'sys_id',
            'name',
            'short_description',
            'description',
            'status',
            'created_at',
            'updated_at'
        )
        read_only_fields = (
            'id',
            'sys_id',
            'created_at',
            'updated_at'
        )
