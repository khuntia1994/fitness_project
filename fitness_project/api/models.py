from django.db import models


class FitnessClass(models.Model):
    Name = models.CharField(max_length=100)
    Instructor = models.CharField(max_length=100)
    Start_time = models.DateTimeField()
    Total_slot = models.PositiveIntegerField()
    Availabel_slot = models.PositiveIntegerField()
    
    def  __str__(self):
        return f"{self.Name} - {self.Start_time}"
    
    
class Booking(models.Model):
    Fitness_class = models.ForeignKey(FitnessClass,on_delete=models.CASCADE)
    Client_name = models.CharField(max_length=100)
    Client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add= True)
