from django.urls import path
from .views import dashboard_uzman_view, degerlendirme_uzman_view
from uzman.views import redirect_to_login

app_name = 'uzman'

urlpatterns = [
    path('dashboard/', dashboard_uzman_view, name='dashboard'),
    path('degerlendirme/', degerlendirme_uzman_view, name='degerlendirme'),
]
