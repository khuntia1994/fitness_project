from django.urls import path
from .import  views
urlpatterns = [
    path('classes/',views.get_classes),
    path('book/',views.book_class),
    path('booking/',views.get_Booking),
    path('cancel/<int:booking_id>/', views.Cancel_booking),
    
]
