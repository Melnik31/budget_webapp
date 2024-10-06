from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Transaction(models.Model):
    store = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.store} | {self.amount} | {self.date}"
    
class Income(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.amount}'