from django.shortcuts import render, redirect, get_object_or_404
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Currency, Transaction
from .serializers import CurrencySerializer, TransactionSerializer
from .forms import CurrencyForm, TransactionForm  # Importe os formulários
from .utils import get_exchange_rate

# Views para a API (DRF)
class CurrencyViewSet(viewsets.ModelViewSet):
    queryset = Currency.objects.all()
    serializer_class = CurrencySerializer

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

@api_view(['GET'])
def api_convert_currency(request):  # Renomeei para evitar conflito
    base_currency = request.query_params.get('base')
    target_currency = request.query_params.get('target')
    if not base_currency or not target_currency:
        return Response(
            {'error': 'Both base and target currencies are required.'},
            status=status.HTTP_400_BAD_REQUEST
        )
    try:
        rate = get_exchange_rate(base_currency, target_currency)
        return Response({'rate': rate})
    except Exception as e:
        error_message = str(e)
        if 'base_currency_access_restricted' in error_message:
            return Response({'error': 'The base currency is restricted or not allowed.'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error': error_message}, status=status.HTTP_400_BAD_REQUEST)

# Views para o frontend (Django Templates)
def currency_list(request):
    currencies = Currency.objects.all()
    return render(request, 'transactions/currency_list.html', {'currencies': currencies})

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'transactions/transaction_list.html', {'transactions': transactions})

def convert_currency(request):
    rate = None
    error = None
    base = request.GET.get('base')
    target = request.GET.get('target')
    currencies = Currency.objects.all()  # Adicione esta linha para obter a lista de moedas

    if base and target:
        try:
            rate = get_exchange_rate(base, target)
        except Exception as e:
            error = str(e)

    return render(request, 'transactions/convert_currency.html', {
        'currencies': currencies,  # Adicione as moedas ao contexto
        'rate': rate,
        'base': base,
        'target': target,
        'error': error,
    })

def currency_create(request):
    if request.method == 'POST':
        form = CurrencyForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('currency_list')
    else:
        form = CurrencyForm()
    return render(request, 'transactions/currency_create.html', {'form': form})

def currency_update(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    if request.method == 'POST':
        form = CurrencyForm(request.POST, instance=currency)
        if form.is_valid():
            form.save()
            return redirect('currency_list')
    else:
        form = CurrencyForm(instance=currency)
    return render(request, 'transactions/currency_form.html', {'form': form})

def currency_delete(request, pk):
    currency = get_object_or_404(Currency, pk=pk)
    if request.method == 'POST':
        currency.delete()
        return redirect('currency_list')
    return render(request, 'transactions/currency_confirm_delete.html', {'currency': currency})

def transaction_create(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm()
    return render(request, 'transactions/transaction_create.html', {'form': form})

def transaction_update(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        form = TransactionForm(request.POST, instance=transaction)
        if form.is_valid():
            form.save()
            return redirect('transaction_list')
    else:
        form = TransactionForm(instance=transaction)
    return render(request, 'transactions/transaction_form.html', {'form': form})

def transaction_delete(request, pk):
    transaction = get_object_or_404(Transaction, pk=pk)
    if request.method == 'POST':
        transaction.delete()
        return redirect('transaction_list')
    return render(request, 'transactions/transaction_confirm_delete.html', {'transaction': transaction})