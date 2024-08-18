from django.contrib import admin
from expense_app.models import (
    ExpenseCategory,
    ExpenseSubCategory,
    Person,
    Account,
    Card,
    Expense
)


# Register your models here.

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):   
    list_display = ('sys_id', 'name', 'short_description', 'status', 'created_at', 'updated_at')


@admin.register(ExpenseSubCategory)
class ExpenseSubCategoryAdmin(admin.ModelAdmin):
    list_display = ('sys_id', 'name', 'category', 'short_description', 'status', 'created_at', 'updated_at')


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('sys_id', 'name', 'short_description', 'status', 'created_at', 'updated_at')


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('sys_id', 'name', 'account_number', 'short_description', 'status', 'created_at', 'updated_at')

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display = ('sys_id', 'account', 'card_type', 'short_description', 'status', 'created_at', 'updated_at')

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('sys_id', 'category', 'person', 'account', 'amount', 'short_description', 'status', 'created_at', 'updated_at')