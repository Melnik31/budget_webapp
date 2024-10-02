from django.urls import path 

from . import views

app_name = 'budgets'
urlpatterns = [
    #home page
    path('', views.index, name='index'),
    path('transactions/', views.transactions, name='transactions'),
    path('delete_one/<int:transaction_id>/', views.delete_one, name='delete_one'),
    path('add_one/', views.add_one, name='add_one'),
    path('edit_transaction/<int:transaction_id>', views.edit_transaction, name='edit_transaction'),
]