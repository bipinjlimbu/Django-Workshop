from django.urls import path
from .views.main_view import form_page, index_page, update_page, delete_page
from .views.auth_view import login_page, register_page

urlpatterns = [
    path('', index_page, name='index'),
    path('login/', login_page, name='login'),
    path('register/',register_page, name='register'),
    path('form/', form_page, name='form'),
    path('update/<int:student_id>/', update_page, name='update'),
    path('delete/<int:student_id>/', delete_page, name='delete'),
]