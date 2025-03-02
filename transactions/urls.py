from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    CurrencyViewSet, TransactionViewSet, api_convert_currency,
    currency_list, transaction_list, convert_currency,
    currency_create, currency_update, currency_delete,
    transaction_create, transaction_update, transaction_delete,
)

# Configuração das URLs da API
router = DefaultRouter()
router.register(r'currencies', CurrencyViewSet)
router.register(r'transactions', TransactionViewSet)

urlpatterns = [
    # URLs da API
    path('api/', include(router.urls)),
    path('api/convert/', api_convert_currency, name='api_convert_currency'),

    # URLs do frontend
    path('currencies/', currency_list, name='currency_list'),
    path('currency/create/', currency_create, name='currency_create'),
    path('currency/<int:pk>/edit/', currency_update, name='currency_update'),
    path('currency/<int:pk>/delete/', currency_delete, name='currency_delete'),
    path('transactions/', transaction_list, name='transaction_list'),
    path('transaction/create/', transaction_create, name='transaction_create'),
    path('transaction/<int:pk>/edit/', transaction_update, name='transaction_update'),
    path('transaction/<int:pk>/delete/', transaction_delete, name='transaction_delete'),
    path('convert/', convert_currency, name='convert_currency'),
]