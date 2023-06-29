from django.contrib import admin
from django.urls import path, include, re_path

from main.views import TodoAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/auth/", include("djoser.urls")),
    re_path(r"^auth/", include("djoser.urls.authtoken")),

    path("api/v1/todo", TodoAPIView.as_view()),
    path("api/v1/todo/<int:pk>", TodoAPIView.as_view()),
]
