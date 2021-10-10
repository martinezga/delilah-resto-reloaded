from django.urls import path
from api import views


urlpatterns = [
    # api/v1/
    path('', views.main_view),
]
