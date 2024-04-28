"""
URL configuration for budgeting_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# budgeting_system/urls.py

from django.contrib import admin
from django.urls import path
from budget import views   # Correct import statement

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('', views.category_list, name='category_list'),
    # path('category/<int:category_id>/add_object/', views.budget_object_create, name='budget_object_create'),
    path('budget/', views.budget, name='category_list'),

    # BOOKS
    path('book/', views.book_list, name='book_list'),
    path('createBook/', views.book_create, name='book_create'),
    path('updateBook/<int:pk>/', views.book_update, name='book_update'),
    path('deleteBook/<int:pk>/', views.book_confirm_delete, name='book_confirm_delete'),
    path('deleteBook/', views.book_delete, name='book_delete'),

    # TVM
    path ('tvm/', views.tvm_list, name='tvm_list'),
    path('createtvm/', views.tvm_create, name='tvm_create'),
    path('deletetvm/<int:pk>/', views.tvm_confirm_delete, name='tvm_confirm_delete'),
    # Define other URLs for update, delete, etc.
    # Define other URLs for update, delete, etc.

]

