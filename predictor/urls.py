from django.urls import path
from .views import data_input_view, result_view
app_name='predictor'
urlpatterns = [
    path('input/',data_input_view, name='data_input'),
    path("result/",result_view,name='result'),
    ]