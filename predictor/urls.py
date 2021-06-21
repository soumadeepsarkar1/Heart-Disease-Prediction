from django.urls import path
from .views import data_input_view, result_view,result_history_view
app_name='predictor'
urlpatterns = [
    path('input/',data_input_view, name='data_input'),
    path("result/",result_view,name='result'),
    path("result_history",result_history_view,name="result_history"),
    ]