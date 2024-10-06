from django import forms

from .models import Transaction
from .models import Income

class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['store', 'amount']

class IncomeForm(forms.ModelForm):
    class Meta:
        model = Income
        fields = ['amount']