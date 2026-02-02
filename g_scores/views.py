from django.shortcuts import render
from django.db.models import F, Value, DecimalField, ExpressionWrapper
from django.db.models.functions import Coalesce
from .models import *
from django.forms.models import model_to_dict

# Create your views here.

def setting(request):
    return render(request, "base.html")

def to_count(scores):
    re = {
        "Từ 8 điểm trở lên": 0,
        "Từ 6 đến 8 điểm": 0,
        "Từ 4 đến 6 điểm": 0,
        "Dưới 4 điểm": 0
    }
    for s in scores:
        if s:
            if s >= 8:
                re["Từ 8 điểm trở lên"] += 1
            elif 6 <= s < 8:
                re["Từ 6 đến 8 điểm"] += 1
            elif 4 <= s < 6:
                re["Từ 4 đến 6 điểm"] += 1
            else:
                re["Dưới 4 điểm"] += 1
    return re

def report(request):
    sub = "toan"
    if request.method == "POST":
        sub = request.POST.get("sub")
    f_scores = Result.objects.values_list(sub, flat=True)
    dict_sub = {
        "toan": "Toán",
        "ngu_van": "Ngữ văn",
        "ngoai_ngu": "Ngoại ngữ",
        "vat_li": "Vật lý",
        "hoa_hoc": "Hóa học",
        "sinh_hoc": "Sinh học",
        "lich_su": "Lịch sử",
        "dia_li": "Địa lý",
        "gdcd" : "GDCD"
    }
    scores_after = to_count(f_scores)
    labels = list(scores_after.keys())
    data = list(scores_after.values())
    return render(request, "report.html", {
        'selected_sub': sub,
        "sub": dict_sub[sub],
        "label": labels,
        "data": data
    })

def search_score(request):
    sbd_check = None
    name_list = None
    scores_after = None
    if request.method == "POST":
        sbd_check = request.POST.get("sbd")
        scores = Result.objects.filter(sbd=sbd_check).first()
        if scores:
            name_list = ["Số báo danh", "Toán", "Ngữ văn", "Ngoại ngữ",\
                "Vật lý", "Hóa học", "Sinh học", "Lịch sử", "Địa lý",\
                "GDCD", "Mã ngoại ngữ"]
            scores_after = model_to_dict(scores)
    return render(request, 'search_scores.html', {
        'scores': scores_after,
        'sbd_check': sbd_check,
        'name_list': name_list
    })

def dash_board(request):
    top_scores = Result.objects.annotate(
        total_score= ExpressionWrapper(Coalesce(F("toan"), Value(0)) +\
            Coalesce(F("vat_li"), Value(0)) +\
                Coalesce(F("hoa_hoc"), Value(0)),\
                output_field = DecimalField(max_digits=5, decimal_places=2))
                ).order_by("-total_score")[:10].values_list('sbd', 'toan', 'vat_li', 'hoa_hoc', 'total_score')
    name_list = ["Số báo danh", "Toán", "Vật lý", "Hóa học", "Tổng điểm"]
    
    return render(request, "dash_board.html", {
        "top_students": top_scores,
        "name_list": name_list,
    })