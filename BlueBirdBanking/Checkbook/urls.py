from django.urls import path
from . import views



urlpatterns = [
    #   Sets the url path to home page index.html
    path('', views.home, name='index'),
    #   Sets url path to Create New Account Page
    path('create/', views.create_account, name='create'),
    #   Sets the url path to balance sheet
    path('<int:pk>/balance/', views.balance, name='balance'),
    #   Sets the url path to Add new transaction
    path('transaction/', views.transaction, name='transaction')
]

