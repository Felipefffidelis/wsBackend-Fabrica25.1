from django.db import models

class Currency(models.Model):
    code = models.CharField(max_length=3, unique=True)  # Ex: USD, BRL, EUR
    name = models.CharField(max_length=50)              # Ex: US Dollar, Brazilian Real

    def __str__(self):
        return self.code

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Valor da transação
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE)  # Moeda associada
    date = models.DateField()                                       # Data da transação
    description = models.TextField()                                # Descrição

    def __str__(self):
        return f"{self.amount} {self.currency.code} on {self.date}"