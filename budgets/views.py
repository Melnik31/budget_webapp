from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Sum

from .models import Transaction

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