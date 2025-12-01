from django.urls import path
from .views.main_view import index_page

urlpatterns = [
    path('index/', index_page, name='index_page'),
]