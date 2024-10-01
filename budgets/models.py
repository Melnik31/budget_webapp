from django.db import models


# Create your models here.

class Transaction(models.Model):
    store = models.CharField(max_length=100)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.store} | {self.amount} | {self.date}"