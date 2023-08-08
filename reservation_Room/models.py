from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class Room(models.Model):
    room_number=models.CharField(max_length=10)
    image1=models.FileField(upload_to="images/")
    image2=models.FileField(upload_to="images/")
    image3=models.FileField(upload_to="images/")
    description=models.TextField()
    capacity=models.IntegerField(default=1)
    pricePerHoure=models.IntegerField()

    def __str__(self):
        return self.room_number
    
    

class Reservation(models.Model):
    user_ID=models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    room_ID=models.ForeignKey(Room, on_delete=models.CASCADE)
    start_time=models.DateTimeField()
    end_time=models.DateTimeField()
    state_active=models.BooleanField()

    def __str__(self):
        return self.user_ID.username