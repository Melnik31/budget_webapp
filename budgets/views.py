from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum

from .models import Transaction
from .forms import TransactionForm

# Create your views here.
def index(requst):
    '''Home page'''
    return render(requst, 'budgets/index.html')

def transactions(request):
    transactions = Transaction.objects.all().order_by('-date')
    total = Transaction.objects.aggregate(Sum('amount'))['amount__sum']
    return render(request, 'budgets/transactions.html', {
        'transactions': transactions,
        'total': total,
    })


def delete_one(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.delete()
    return redirect('budgets:transactions')

def add_one(request):
    if request.method != 'POST':
        form = TransactionForm()
    else:
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('budgets:transactions')
        
    context = {'form': form}
    return render(request, 'budgets/add_one.html', context)

def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    
    if request.method != 'POST':
        form = TransactionForm(instance=transaction)
    else:
        form = TransactionForm(instance=transaction, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('budgets:transactions')
        
    context = {'form': form, 'transaction': transaction}
    return render(request, 'budgets/edit_transaction.html', context)

