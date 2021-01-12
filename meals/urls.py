from django.urls import path

from .views import MealsListView, OrderView

app_name = 'meals'

urlpatterns = [
    path('', MealsListView.as_view(), name='index'),
    path('create_order/', OrderView.as_view(), name='create_order'),
]
