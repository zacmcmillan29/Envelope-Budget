from django.db import models

# Create your models here.
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class BudgetObject(models.Model):
    name = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    publication_date = models.DateField()

    def __str__(self):
        return self.title


class TVM(models.Model):
    employee = models.CharField(max_length=100)
    phase = models.CharField(max_length=100)
    deliverable = models.CharField(max_length=100)
    task = models.CharField(max_length=100)
    hoursWorked = models.IntegerField(max_length=100)

    def __str__(self):
        return self.task
