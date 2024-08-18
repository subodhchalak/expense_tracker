from rest_framework.viewsets import ModelViewSet

from expense_app.models import (
    ExpenseCategory,
    ExpenseSubCategory,
    Person
)
from expense_app.serializers import (
    ExpenseCategorySerializer,
    ExpenseSubCategorySerializer,
    PersonSerializer
)

# Create your views here.

# ---------------------------- ExpenseCategoryMVS ---------------------------- #

class ExpenseCategoryMVS(ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer
    
# --------------------------- ExpenseSubCategoryMVS -------------------------- #

class ExpenseSubCategoryMVS(ModelViewSet):
    queryset = ExpenseSubCategory.objects.all()
    serializer_class = ExpenseSubCategorySerializer

# --------------------------- ExpenseSubCategoryMVS -------------------------- #

class PersonMVS(ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer