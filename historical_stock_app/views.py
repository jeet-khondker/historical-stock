from django.shortcuts import render
from django.views.generic import ListView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

import requests
import os

from .models import HistoricalStockPrice

# Function : Pagination Query
def paginate_query(request, queryset, count):
    paginator = Paginator(queryset, count)
    page = request.GET.get("page")

    try:
        page_obj = paginator.page(page)
    except PageNotAnInteger:
        page_obj = paginator.page(1)
    except EmptyPage:
        page_obj = paginator.page(paginator.num_pages)

    return page_obj

# Historical Stock List View
class HistoricalStockListView(ListView):

    template_name = "historical_stock/historical_stock_list.html"

    def get(self, request, *args, **kwargs):
        all_historical_stock = {}

        url = "https://financialmodelingprep.com/api/v3/historical-price-full/AAPL,GOOG,AMZN?apikey="

        response = requests.get(url + os.getenv("API_KEY"))

        data = response.json()

        companies = data["historicalStockList"]

        # If there is no previous data in database
        if not HistoricalStockPrice.objects.all().exists():

            for company in companies:
                for historical_data in company["historical"]:
                    historical_stock_data = HistoricalStockPrice(
                        companySymbol = company["symbol"],
                        historicalDate = historical_data["date"],
                        historicalOpen = historical_data["open"],
                        historicalHigh = historical_data["high"],
                        historicalLow = historical_data["low"],
                        historicalClose = historical_data["close"],
                        historicalAdjClose = historical_data["adjClose"],
                        historicalVolume = historical_data["volume"],
                        historicalUnAdjustedVolume = historical_data["unadjustedVolume"],
                        historicalChange = historical_data["change"],
                        historicalChangePercent = historical_data["changePercent"],
                        historicalVwap = historical_data["vwap"],
                        historicalLabel = historical_data["label"],
                        historicalChangeOverTime = historical_data["changeOverTime"]
                    )
                    
                    historical_stock_data.save()

                    all_historical_stock = HistoricalStockPrice.objects.all().order_by("id")
                    # all_historical_stock = HistoricalStockPrice.objects.all().order_by("id")[:100]

                    page_obj = paginate_query(request, all_historical_stock, 100)

            return render(request, self.template_name, { "page_obj" : page_obj })

        # Else (if there is data already inside the database)
        all_historical_stock = HistoricalStockPrice.objects.all().order_by("id")
        page_obj = paginate_query(request, all_historical_stock, 100)

        return render(request, self.template_name, { "page_obj" : page_obj })