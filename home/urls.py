from django.urls import path
from home.views import ServiceWorkerView, TestView

urlpatterns = [
    path("", TestView.as_view(), name="test"),
    path(
        "sw.js",
        ServiceWorkerView.as_view(),
        name=ServiceWorkerView.name,
    ),

]
