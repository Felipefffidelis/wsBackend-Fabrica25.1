import requests
from django.conf import settings
import logging

logger = logging.getLogger(__name__)

def get_exchange_rate(base_currency, target_currency):
    url = f"https://data.fixer.io/api/latest?access_key={settings.FIXER_API_KEY}&base={base_currency}&symbols={target_currency}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Verifica se houve algum erro na requisição
        data = response.json()
        logger.debug(f"API response: {data}")
        if data.get('success'):
            return data['rates'].get(target_currency)
        else:
            raise Exception(f"API error: {data.get('error', 'Unknown error')}")
    except requests.exceptions.RequestException as e:
        logger.error(f"HTTP request failed: {e}")
        raise Exception(f"HTTP request failed: {e}")