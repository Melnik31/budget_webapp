from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.http import Http404

from .models import Transaction
from .forms import TransactionForm

# Create your views here.
def index(requst):
    '''Home page'''
    return render(requst, 'budgets/index.html')

@login_required
def transactions(request):
    transactions = Transaction.objects.filter(owner=request.user).order_by('-date')
    total = Transaction.objects.filter(owner=request.user).aggregate(Sum('amount'))['amount__sum'] or 0
    return render(request, 'budgets/transactions.html', {
        'transactions': transactions,
        'total': total,
    })

@login_required
def delete_one(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    transaction.delete()
    return redirect('budgets:transactions')

@login_required
def add_one(request):
    
    if request.method != 'POST':
        form = TransactionForm()
    else:
        form = TransactionForm(data=request.POST)
        if form.is_valid():
            add_one = form.save(commit=False)
            add_one.owner = request.user
            add_one.save()
            return redirect('budgets:transactions')
        
    context = {'form': form}
    return render(request, 'budgets/add_one.html', context)

@login_required
def edit_transaction(request, transaction_id):
    transaction = get_object_or_404(Transaction, id=transaction_id)
    if transaction.owner != request.user:
        raise Http404
    
    if request.method != 'POST':
        form = TransactionForm(instance=transaction)
    else:
        form = TransactionForm(instance=transaction, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('budgets:transactions')
        
    context = {'form': form, 'transaction': transaction}
    return render(request, 'budgets/edit_transaction.html', context)

