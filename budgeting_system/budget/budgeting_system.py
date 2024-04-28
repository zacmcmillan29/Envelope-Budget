# # budget/budgeting_system.py
from django.db import models


##### OLD WAY, didn't work ####
# class BudgetingSystem:
#     @staticmethod
#     def set_budget(categories, available_cash):
#         total_budget = sum(category.budgetobject_set.aggregate(models.Sum('amount'))['amount__sum'] or 0 for category in categories)
#         for category in categories:
#             category_budget = category.budgetobject_set.aggregate(models.Sum('amount'))['amount__sum'] or 0
#             category_percentage = category_budget / total_budget if total_budget != 0 else 0
#             category.budget_amount = available_cash * category_percentage
#             category.save()


from .models import models

class BudgetingSystem:
    @staticmethod
    def set_budget(categories, available_cash):
        total_budget = sum(category.budgetobject_set.aggregate(models.Sum('amount'))['amount__sum'] or 0 for category in categories)
        for category in categories:
            category_budget = category.budgetobject_set.aggregate(models.Sum('amount'))['amount__sum'] or 0
            category_percentage = category_budget / total_budget if total_budget != 0 else 0
            category.budget_amount = available_cash * category_percentage
            category.save()
