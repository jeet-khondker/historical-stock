from django.shortcuts import render

from django.views.generic import ListView

# Historical Stock List View
class HistoricalStockListView(ListView):

    template_name = "historical_stock/historical_stock_list.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
