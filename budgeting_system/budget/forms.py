from django import forms
from .models import BudgetObject, Book, TVM

class BudgetObjectForm(forms.ModelForm):
    class Meta:
        model = BudgetObject
        fields = ['name', 'amount', 'category']

\

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'publication_date']


class TVMForm(forms.ModelForm):
    class Meta:
        model = TVM
        fields = ['employee', 'phase', 'deliverable', 'task', 'hoursWorked']
