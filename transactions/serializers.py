from rest_framework import serializers
from .models import Currency, Transaction

class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['id', 'code', 'name']

class TransactionSerializer(serializers.ModelSerializer):
    currency = CurrencySerializer(read_only=True)  # Para leitura
    currency_id = serializers.PrimaryKeyRelatedField(
        queryset=Currency.objects.all(), source='currency', write_only=True
    )  # Para escrita

    class Meta:
        model = Transaction
        fields = ['id', 'amount', 'currency', 'currency_id', 'date', 'description']