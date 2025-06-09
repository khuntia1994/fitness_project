from rest_framework.decorators import api_view
from rest_framework.response import Response
from . models import FitnessClass,Booking
from django.utils.timezone import now
from .serializer import FitnessClassSerializer,BookingSerializer,CreateBookingSerializer



@api_view(['GET'])
def get_classes(request):
    classes = FitnessClass.objects.filter(Start_time__gte=now()).order_by('Start_time')
    serializer = FitnessClassSerializer(classes, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def book_class (request):
    serializer = CreateBookingSerializer(data = request.data)
    if serializer.is_valid():
        try:
            fitness_class = FitnessClass.objects.get(id = serializer.validated_data['Class_Id'])
            if fitness_class.Availabel_slot <= 0:
                return Response ({'error':'no slot available'},status = 400)
            
            Booking.objects.create(
                Fitness_class = fitness_class, 
                Client_name = serializer.validated_data['Client_name'],
                Client_email = serializer.validated_data['Client_email']
            )
            fitness_class.Availabel_slot -= 1
            fitness_class.save()
            return Response ({'message':'Booking Successfull..'})
        
        
        
        
        
        
        except FitnessClass.DoesNotExist:
            return Response({'error':'Invalid class ID.....'},status=400)
    return Response(serializer.errors,status=400)


@api_view(['GET'])
def get_Booking (request):
    email = request.GET.get('email')
    if not email:
        return Response({'error':'Email is required'},status=400)
    bookings = Booking.objects.filter(Client_email = email)
    serializer = BookingSerializer(bookings,many =True)
    return Response(serializer.data)



@api_view(['DELETE'])
def Cancel_booking(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id)
    except Booking.DoesNotExist:
        return Response({'error': 'Booking not found'}, status=404)

    fitness_class = booking.Fitness_class
    fitness_class.Availabel_slot += 1
    fitness_class.save()

    booking.delete()
    return Response({'message': 'Booking cancelled successfully.'}, status=200)