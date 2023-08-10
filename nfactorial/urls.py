from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<int:first>/add/<int:second>/", views.sum, name="sum"),
    path("transform/<str:text>", views.uppercase, name="uppercase"),
    path("check/<str:word>/", views.is_palindrome, name="is_palindrome"),
    path("calc/<int:first>/<str:operation>/<int:second>/", views.calculator, name="calculator"),
]