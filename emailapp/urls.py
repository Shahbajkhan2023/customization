from django.urls import path
from .views import send_email_view, email_success

urlpatterns = [
    path('send-email/', send_email_view, name='send_email'),
    path('email-success/', email_success, name='email_success'),
]
