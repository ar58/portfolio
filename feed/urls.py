from django.urls import path
from .views import HomeView,ContactFormView

app_name = 'feed'

urlpatterns = [
    path('',HomeView.as_view(),name='home'),
    path('post',ContactFormView.as_view(),name='post'),
]
