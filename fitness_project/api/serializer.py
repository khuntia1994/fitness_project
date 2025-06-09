from rest_framework import serializers
from .models import FitnessClass,Booking


class FitnessClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = FitnessClass
        fields = '__all__'
        
        
class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'
        
        
class CreateBookingSerializer(serializers.Serializer):
    Class_Id = serializers.IntegerField()
    Client_name = serializers.CharField()
    Client_email = serializers.EmailField()
        
        