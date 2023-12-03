from django.shortcuts import render
from django.db.models.functions import Rank
from django.db.models import Window
from .models import RankTest


# Create your views here.

def index(request):
    rank_list = RankTest.objects.annotate(
        rank=Window(
            expression=Rank(),
            order_by='rating'
        )
    )
    context = {'rank_list': rank_list}
    return render(request, 'rank/index.html', context)
