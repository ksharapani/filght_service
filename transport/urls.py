from django.urls import path


from .views import *

urlpatterns = [
    path('bookings', BookingView.as_view(), name='bookings'),
    path('history', BookingHistoryView.as_view(), name='history'),
]
