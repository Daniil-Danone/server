from django.contrib import admin
from django.urls import path, include, re_path

from main.views import MarksAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),

    path("api/v1/mark", MarksAPIView.as_view()),
    path("api/v1/mark/<int:pk>", MarksAPIView.as_view()),
]
