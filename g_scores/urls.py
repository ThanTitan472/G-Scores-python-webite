from django.urls import path
from .views import *

urlpatterns = [
    path('', dash_board, name='dash-board'),
    path('dashboard/', dash_board, name='dash-board'),

    path('searchscores/', search_score, name='search-scores'),

    path('reports/', report, name='reports'),

    path('settings/', setting, name='settings')
]