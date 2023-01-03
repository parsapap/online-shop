from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('profile/<int:user_id>/', views.ProfileApiView.as_view(), name='profile_api'),
    path('profile/edit/<int:user_id>/', views.ProfileEditApiView.as_view(), name='profile_edit_api'),
]
