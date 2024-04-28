from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from .models import Category, Book, TVM
from .models import BudgetObject
from .forms import BudgetObjectForm, BookForm, TVMForm
from .budgeting_system import BudgetingSystem

# def category_list(request):
#     categories = Category.objects.all()
#     BudgetingSystem.set_budget(categories, available_cash=1000)  # Example: Set available cash to $1000
#     return render(request, 'budget/category_list.html', {'categories': categories})

# # def budget_object_create(request):
#     if request.method == 'POST':
#         form = BudgetObjectForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('category_list')
#     else:
#         form = BudgetObjectForm()
#     return render(request, 'budget/budget_object_form.html', {'form': form})

def budget (request):
    return render (request, 'budget/category_list.html')


# BOOK #
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/book_form.html', {'form': form})

def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/book_form.html', {'form': form})

def book_confirm_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/book_confirm_delete.html', {'book': book})

def book_delete(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        book = Book.objects.filter(title=title, author=author).first()
        if book:
            book.delete()
            return redirect('book_list')
        else:
            return HttpResponse("Book not found.")
    else:
        return HttpResponse("Invalid request method.")
    


# TVM view##
def tvm_list(request):
    tvms = TVM.objects.all()
    return render(request, 'time value management/tvm_list.html', {'tvms': tvms})

def tvm_create(request):
    if request.method == 'POST':
        form = TVMForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('tvm_list')
    else:
        form = TVMForm()
    return render(request, 'time value management/tvm_form.html', {'form': form})

def tvm_confirm_delete(request, pk):
    tvm = get_object_or_404(TVM, pk=pk)
    if request.method == 'POST':
        tvm.delete()
        return redirect('tvm_list')
    return render(request, 'time value management/tvm_confirm_delete.html', {'tvm': tvm})