# from rest_framework import generics
# from rest_framework.pagination import PageNumberPagination
# from rest_framework.permissions import IsAuthenticated
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from django.conf import settings

# from .models import Coin, Category
# from .serializers import CoinSerializer, CategorySerializer

# class CoinPagination(PageNumberPagination):
#     page_size = 10
#     page_size_query_param = 'per_page'

# class CoinListView(generics.ListAPIView):
#     queryset = Coin.objects.all()
#     serializer_class = CoinSerializer
#     pagination_class = CoinPagination
#     permission_classes = [IsAuthenticated]

# class CategoryListView(generics.ListAPIView):
#     queryset = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [IsAuthenticated]

# class CoinDetailView(generics.RetrieveAPIView):
#     queryset = Coin.objects.all()
#     serializer_class = CoinSerializer
#     permission_classes = [IsAuthenticated]

# class CoinsByCategoryView(generics.ListAPIView):
#     serializer_class = CoinSerializer
#     pagination_class = CoinPagination
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         category_id = self.kwargs['category_id']
#         return Coin.objects.filter(categories__id=category_id)

# class HealthCheckView(APIView):
#     def get(self, request):
#         # Simplified health check
#         return Response({'status': 'healthy'})

# class VersionView(APIView):
#     def get(self, request):
#         version_info = {
#             'version': '1.0',
#             'description': 'Crypto API'
#         }
#         return Response(version_info)


from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Coin, Category
from .serializers import CoinSerializer, CategorySerializer

class CoinPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = 'per_page'

class CoinListView(generics.ListAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    pagination_class = CoinPagination
    permission_classes = [IsAuthenticated]

class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAuthenticated]

class CoinDetailView(generics.RetrieveAPIView):
    queryset = Coin.objects.all()
    serializer_class = CoinSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'coin_id'  # Set lookup_field to use coin_id

class CoinsByCategoryView(generics.ListAPIView):
    serializer_class = CoinSerializer
    pagination_class = CoinPagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Coin.objects.filter(categories__id=category_id)

class HealthCheckView(APIView):
    def get(self, request):
        return Response({'status': 'healthy'})

class VersionView(APIView):
    def get(self, request):
        version_info = {
            'version': '1.0',
            'description': 'Crypto API'
        }
        return Response(version_info)
