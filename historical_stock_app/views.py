from django.shortcuts import render

from django.views.generic import ListView

# Historical Stock List View
class HistoricalStockListView(ListView):

    def get(self, request, *args, **kwargs):
        return render(request, "historical_stock/historical_stock_list.html")
