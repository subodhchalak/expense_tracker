# Generated by Django 5.0.7 on 2024-08-04 13:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expense_app', '0004_expensesubcategory_alter_expensecategory_created_at_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expensesubcategory',
            options={'ordering': ['-id'], 'verbose_name': 'ExpenseSubCategory', 'verbose_name_plural': 'ExpenseSubCategories'},
        ),
    ]
