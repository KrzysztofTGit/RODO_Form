from django.contrib import admin
from django.urls import path
from rodo_app.views import FormView, ConfirmationView, FormFinishedView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('join/<str:form_url>/', FormView.as_view(), name="join"),
    path('form-finished/', FormFinishedView.as_view(), name="form"),
    path('confirm/<str:user_url>/', ConfirmationView.as_view(), name="confirmation"),
]
