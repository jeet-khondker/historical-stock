from django.urls import path
from historical_stock_app.views import HistoricalStockListView

urlpatterns = [
    path('', HistoricalStockListView.as_view(), name="get_historical_stock"),
]