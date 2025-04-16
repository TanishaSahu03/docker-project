from app import views
from django.urls import path, include

urlpatterns = [
    path("create/", views.StudentCreate.as_view(), name = "create"),

]
