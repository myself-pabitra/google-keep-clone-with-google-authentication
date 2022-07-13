from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('addnote', addnote, name='addnote'),
    path('edit/<str:pk>', edit_note, name='edit'),
    path('delete/<str:pk>', delete_note, name='delete'),
    path('register', register_page, name='register'),
    path('accounts/login', login_page, name='login'),
    path('logout', logout_user, name='logout'),
    path('search', search_note, name='search'),
]
