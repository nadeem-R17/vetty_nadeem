# from django.urls import path
# from .views import CoinListView, CategoryListView, CoinDetailView, CoinsByCategoryView
# from .views import HealthCheckView, VersionView

# urlpatterns = [
#     path('coins/', CoinListView.as_view(), name='coin-list'),
#     path('categories/', CategoryListView.as_view(), name='category-list'),
#     path('coins/<str:coin_id>/', CoinDetailView.as_view(), name='coin-detail'),
#     path('categories/<int:category_id>/coins/', CoinsByCategoryView.as_view(), name='coins-by-category'),
#     # path('coins/<str:pk>/', CoinDetailView.as_view(), name='coin-detail'),
#     # path('categories/<int:category_id>/coins/', CoinsByCategoryView.as_view(), name='coins-by-category'),
#     path('health/', HealthCheckView.as_view(), name='health-check'),
#     path('version/', VersionView.as_view(), name='version-info'),
# ]



from django.urls import path
from .views import CoinDetailView, CoinListView, CategoryListView, CoinsByCategoryView, HealthCheckView, VersionView

urlpatterns = [
    path('coins/', CoinListView.as_view(), name='coin-list'),
    path('coins/<int:pk>/', CoinDetailView.as_view(), name='coin-detail'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('categories/<int:category_id>/coins/', CoinsByCategoryView.as_view(), name='coins-by-category'),
    path('health/', HealthCheckView.as_view(), name='health-check'),
    path('version/', VersionView.as_view(), name='version-info'),
]
