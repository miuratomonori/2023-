from django.views.generic import TemplateView
from django.shortcuts import render
#以下設定
import pandas as pd             #データ解析ライブラリ

from PIL import Image           #画像処理ライブラリ

import copy                     #コピーできる(ディープコピー)

from . import graph

# Create your views here.

#month_data = pd.read_csv('/data/月/mth_date.csv')
#day_data = pd.read_csv('/data/日/day_date.csv')

def index_template(request):

    return render(request, 'index.html')

def graphCreatData(request):
    return()


