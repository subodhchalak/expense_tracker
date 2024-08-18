from django.db import models

# Create your models here.


# ---------------------------------------------------------------------------- #
#                                ExpenseCategory                               #
# ---------------------------------------------------------------------------- #

class ExpenseCategory(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        help_text="It is the name of the expense category",
        unique=True,
        blank=False
    )
    short_description = models.CharField(
        verbose_name="Short Description",
        max_length=250,
        help_text="It is the short description of the expense category",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
        help_text="It is the description of the expense category",
        blank=True
    )
    status = models.BooleanField(
        verbose_name="Activation Status",
        default=True,
        help_text="It is the activation status of the expense category"
    )
    created_at = models.DateTimeField(
        verbose_name="Create Date Time",
        help_text="It is the category's create date and time",
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Update Date Time",
        help_text="It is the category's update date and time",
        auto_now_add=True
    )

    class Meta:
        ordering=["-id"]
        verbose_name="ExpenseCategory"
        verbose_name_plural="ExpenseCategories"

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    @property
    def sys_id(self):
        return "EX-CAT-{}".format(str(self.id).zfill(6))
    
    
# ---------------------------------------------------------------------------- #
#                              ExpenseSubCategory                              #
# ---------------------------------------------------------------------------- #


class ExpenseSubCategory(models.Model):
    category = models.ForeignKey(
        to=ExpenseCategory,
        on_delete=models.CASCADE,
        related_name='expense_sub_category',
        verbose_name="Category",
        help_text="This is the category of the sub category.",
        null=True
    )
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        help_text="It is the name of the expense sub category",
        unique=True,
        blank=False
    )
    short_description = models.CharField(
        verbose_name="Short Description",
        max_length=250,
        help_text="It is the short description of the expense sub category",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
        help_text="It is the description of the expense sub category",
        blank=True
    )
    status = models.BooleanField(
        verbose_name="Activation Status",
        default=True,
        help_text="It is the activation status of the expense sub category"
    )
    created_at = models.DateTimeField(
        verbose_name="Create Date Time",
        help_text="It is the sub category's create date and time",
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Update Date Time",
        help_text="It is the sub category's update date and time",
        auto_now_add=True
    )

    class Meta:
        ordering=["-id"]
        verbose_name="ExpenseSubCategory"
        verbose_name_plural="ExpenseSubCategories"

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    @property
    def sys_id(self):
        return "EX-SUB-CAT-{}".format(str(self.id).zfill(6))
    
# ---------------------------------------------------------------------------- #
#                                    Person                                    #
# ---------------------------------------------------------------------------- #

class Person(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        help_text="It is the name of the person",
        unique=True,
        blank=False
    )
    short_description = models.CharField(
        verbose_name="Short Description",
        max_length=250,
        help_text="It is the short description of the person",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
        help_text="It is the description of the person",
        blank=True
    )
    status = models.BooleanField(
        verbose_name="Activation Status",
        default=True,
        help_text="It is the activation status of the person"
    )
    created_at = models.DateTimeField(
        verbose_name="Create Date Time",
        help_text="It is the person's create date and time",
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Update Date Time",
        help_text="It is the person's update date and time",
        auto_now_add=True
    )

    class Meta:
        ordering=["-id"]
        verbose_name="Person"
        verbose_name_plural="Persons"

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    @property
    def sys_id(self):
        return "EX-PRSN-{}".format(str(self.id).zfill(6))


# ---------------------------------------------------------------------------- #
#                                    Account                                   #
# ---------------------------------------------------------------------------- #


class Account(models.Model):
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        help_text="It is the name of the account",
        unique=True,
        blank=False
    )
    account_number = models.CharField(
        verbose_name="Name",
        max_length=50,
        help_text="It is the account number",
        unique=True,
        blank=False
    )
    short_description = models.CharField(
        verbose_name="Short Description",
        max_length=250,
        help_text="It is the short description of the account",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
        help_text="It is the description of the account",
        blank=True
    )
    status = models.BooleanField(
        verbose_name="Activation Status",
        default=True,
        help_text="It is the activation status of the account"
    )
    created_at = models.DateTimeField(
        verbose_name="Create Date Time",
        help_text="It is the accounts's create date and time",
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Update Date Time",
        help_text="It is the accounts's update date and time",
        auto_now_add=True
    )

    class Meta:
        ordering=["-id"]
        verbose_name="Account"
        verbose_name_plural="Accounts"

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    @property
    def sys_id(self):
        return "EX-ACNT-{}".format(str(self.id).zfill(6))
    
# ---------------------------------------------------------------------------- #
#                                     Card                                     #
# ---------------------------------------------------------------------------- #

class Card(models.Model):
    card_type_choices = (
        ('credit', 'Credit'),
        ('debit', 'Debit')
    )
    account = models.ForeignKey(
        to=Account,
        on_delete=models.SET_NULL,
        related_name='card',
        null=True,
        blank=False
    )
    card_type = models.CharField(
        max_length=50,
        choices=card_type_choices,
        null=False,
        blank=False,
    )
    card_number = models.CharField(
        max_length=50,
        null=False,
        blank=False,
    ),
    name = models.CharField(
        verbose_name="Name",
        max_length=50,
        help_text="It is the name of the card",
        unique=True,
        blank=False
    )
    short_description = models.CharField(
        verbose_name="Short Description",
        max_length=250,
        help_text="It is the short description of the card",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
        help_text="It is the description of the card",
        blank=True
    )
    status = models.BooleanField(
        verbose_name="Activation Status",
        default=True,
        help_text="It is the activation status of the card"
    )
    created_at = models.DateTimeField(
        verbose_name="Create Date Time",
        help_text="It is the card's create date and time",
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Update Date Time",
        help_text="It is the card's update date and time",
        auto_now_add=True
    )

    class Meta:
        ordering=["-id"]
        verbose_name="Card"
        verbose_name_plural="Cards"

    def __str__(self):
        return f"{self.id} - {self.name}"
    
    @property
    def sys_id(self):
        return "EX-CARD-{}".format(str(self.id).zfill(6))

# ---------------------------------------------------------------------------- #
#                                    Expense                                   #
# ---------------------------------------------------------------------------- #


class Expense(models.Model):
    mode_choices = (
       ('cash', 'Cash'),
       ('card', 'Card'),
       ('cheque', 'Cheque'),
       ('demand_draft', 'Demand Draft'),
       ('upi', 'UPI'),
       ('net_banking', 'Net Banking')
    )

    category = models.ForeignKey(
        to=ExpenseCategory,
        on_delete=models.SET_NULL,
        related_name='expense',
        verbose_name='Category',
        help_text="Category name of the expense",
        null=True,
        blank=False
    )
    person = models.ForeignKey(
        to=Person,
        on_delete=models.SET_NULL,
        related_name='expense',
        help_text="Person for which expense occurred",
        null=True,
        blank=True
    )
    account = models.ForeignKey(
        to=Account,
        on_delete=models.SET_NULL,
        related_name='expense',
        help_text="Account from which expense occurred",
        null=True,
        blank=True
    )
    amount = models.FloatField(
        verbose_name='Amount',
        default=0,
        null=False,
        blank=False,
        help_text="Enter the expense amount"
    )
    transaction_id = models.CharField(
        verbose_name='Transaction ID',
        max_length=100,
        blank=True,
        help_text="Enter the transaction ID"
    )
    benificiary = models.CharField(
        verbose_name='Benificary Name',
        max_length=100,
        blank=True,
        help_text="Enter the name of the beficiary"
    )
    mode = models.CharField(
        verbose_name='Expense Mode',
        max_length=50,
        null=False,
        blank=False,
        choices=mode_choices
    )
    short_description = models.CharField(
        verbose_name="Short Description",
        max_length=250,
        help_text="It is the short description of the account",
        blank=True
    )
    description = models.TextField(
        verbose_name="Description",
        max_length=1000,
        help_text="It is the description of the account",
        blank=True
    )
    status = models.BooleanField(
        verbose_name="Activation Status",
        default=True,
        help_text="It is the activation status of the account"
    )
    created_at = models.DateTimeField(
        verbose_name="Create Date Time",
        help_text="It is the expense's create date and time",
        auto_now=True
    )
    updated_at = models.DateTimeField(
        verbose_name="Update Date Time",
        help_text="It is the expense's update date and time",
        auto_now_add=True
    )

    class Meta:
        ordering=["-id"]
        verbose_name="Expense"
        verbose_name_plural="Expenses"

    def __str__(self):
        return f"{self.id} - {self.amount}"
    
    @property
    def sys_id(self):
        return "EX-EXP-{}".format(str(self.id).zfill(6))
