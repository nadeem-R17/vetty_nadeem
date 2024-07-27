from django.urls import path

from .views import (CategoryListView, CoinDetailView, CoinListView,
                    CoinsByCategoryView, HealthCheckView, VersionView)

urlpatterns = [
    path("coins/", CoinListView.as_view(), name="coin-list"),
    path("coins/<int:pk>/", CoinDetailView.as_view(), name="coin-detail"),
    path("categories/", CategoryListView.as_view(), name="category-list"),
    path(
        "categories/<int:category_id>/coins/",
        CoinsByCategoryView.as_view(),
        name="coins-by-category",
    ),
    path("health/", HealthCheckView.as_view(), name="health-check"),
    path("version/", VersionView.as_view(), name="version-info"),
]
