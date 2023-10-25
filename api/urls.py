from django.contrib import admin
from django.urls import path, include
from . import views


from api.views import profile_view

urlpatterns = [
    path('profile',profile_view, name="profile"),
    path('skintypes/', views.SkinTypeList.as_view(), name='skintype-list'),
]
