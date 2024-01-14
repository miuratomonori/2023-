from django.views.generic import TemplateView
from django.shortcuts import render
#以下設定
import pandas as pd             #データ解析ライブラリ

from PIL import Image           #画像処理ライブラリ

import copy                     #コピーできる(ディープコピー)

from . import graph

# Create your views here.

demo_data = pd.read_csv('C:/Users/owner/python-2023/testproject/static/csv/year_date.csv')
#day_data = pd.read_csv('/data/日/day_date.csv')

def index_template(request):

    return render(request, 'index.html')

def graphCreatData(request):
    #グラフオブジェクト
        a = 1
        qs    = demo_data  #モデルクラス(ProductAテーブル)読込
        x     = [x.Date for x in qs]           #X軸データ
        y     = [y.Revenue for y in qs]        #Y軸データ
        chart = graph.Plot_Graph(x,y)          #グラフ作成

        #変数を渡す
        context = super().get_context_data(**kwargs)
        context['chart'] = chart
    #return(a)


