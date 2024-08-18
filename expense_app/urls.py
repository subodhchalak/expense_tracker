from django.urls import path

# third party imports
from rest_framework.routers import DefaultRouter

from expense_app.views import (
    ExpenseCategoryMVS,
    ExpenseSubCategoryMVS,
    PersonMVS
)



router = DefaultRouter()
router.register(r'^category', ExpenseCategoryMVS, basename='category')
router.register(r'^sub_category', ExpenseSubCategoryMVS, basename='sub_category')
router.register(r'^person', PersonMVS, basename='person')

urlpatterns = []

# adding router urls
urlpatterns += router.urls