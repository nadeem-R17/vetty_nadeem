from rest_framework import serializers
from .models import Coin, Category
import requests
from django.conf import settings

class CoinSerializer(serializers.ModelSerializer):
    market_data = serializers.SerializerMethodField()

    class Meta:
        model = Coin
        fields = '__all__'

    def get_market_data(self, obj):
        url = f'https://api.coingecko.com/api/v3/coins/{obj.coin_id}'
        params = {
            'localization': 'false',
            'x_cg_demo_api_key': settings.COINGECKO_API_KEY,
        }
        response = requests.get(url, params=params)
        return response.json()

class CategorySerializer(serializers.ModelSerializer):
    coins = CoinSerializer(many=True, read_only=True)

    class Meta:
        model = Category
        fields = '__all__'



# from rest_framework import serializers
# from .models import Coin, Category

# class CoinSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Coin
#         fields = '__all__'

# class CategorySerializer(serializers.ModelSerializer):
#     coins = CoinSerializer(many=True, read_only=True)

#     class Meta:
#         model = Category
#         fields = '__all__'
