import os
from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse

from . import database
from .models import Item, Bid

# generic views
from django.views.generic import (
	ListView, DetailView, CreateView, UpdateView, DeleteView
)

from datetime import datetime
import pytz
# list views
class ItemListView(ListView):
    model = Item
    template_name = 'welcome/base.html'
    context_object_name = 'object'
    ordering = ['-date_end']
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        items = Item.objects.filter(date_end__gt = datetime.now(pytz.UTC))
        bids = []
        for item in items:
            bids_queryset = Bid.objects.filter(item = item).order_by('-price')
            if bids_queryset.exists():
                bids.append(bids_queryset.first())
        context.update({
        'items': items,
        'bids': bids,
        })
        return context
