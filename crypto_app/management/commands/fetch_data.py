import requests
from django.core.management.base import BaseCommand
from django.conf import settings
from crypto_app.models import Coin, Category

class Command(BaseCommand):
    help = 'Fetch cryptocurrency data from CoinGecko API'

    def handle(self, *args, **kwargs):
        coin_url = 'https://api.coingecko.com/api/v3/coins/markets'
        category_url = 'https://api.coingecko.com/api/v3/coins/categories'
        
        params = {
            'vs_currency': 'cad',
            'x_cg_demo_api_key': settings.COINGECKO_API_KEY,
        }
        
        coin_response = requests.get(coin_url, params=params)
        category_response = requests.get(category_url, params={'x_cg_demo_api_key': settings.COINGECKO_API_KEY})

        coin_data = coin_response.json()
        category_data = category_response.json()

        for item in coin_data:
            Coin.objects.update_or_create(
                coin_id=item['id'],
                defaults={
                    'name': item['name'],
                    'symbol': item['symbol'],
                }
            )

        for item in category_data:
            category, created = Category.objects.update_or_create(
                name=item['name'],
            )
            # Add coins to categories if necessary

        self.stdout.write(self.style.SUCCESS('Successfully fetched data'))


# import requests
# from django.core.management.base import BaseCommand
# from crypto_app.models import Coin, Category

# class Command(BaseCommand):
#     help = 'Fetch cryptocurrency data from CoinGecko API'

#     def handle(self, *args, **kwargs):
#         response = requests.get('https://api.coingecko.com/api/v3/coins/markets', params={'vs_currency': 'cad'})
#         data = response.json()

#         for item in data:
#             coin, created = Coin.objects.update_or_create(
#                 coin_id=item['id'],
#                 defaults={
#                     'name': item['name'],
#                     'symbol': item['symbol'],
#                 }
#             )
#         self.stdout.write(self.style.SUCCESS('Successfully fetched data'))
