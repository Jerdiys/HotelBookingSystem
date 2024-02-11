from django.db import models
from django.contrib.auth.models import User
import random

def generatebookingcode():
    code = ""
    for i in range(7):
        number = str(random.randint(0, 9))
        code += number

    return code


# Create your models here.
class Room(models.Model):
    roomtype = models.CharField(max_length=255)
    roomprice = models.IntegerField()
    roomphoto = models.ImageField(upload_to='images/')
    

    def __str__(self):
        return self.roomtype
    


class RoomBooking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    roomtype = models.ForeignKey(Room, on_delete=models.CASCADE)
    check_in_date = models.DateField()
    check_out_date = models.DateField()
    booking_code = models.CharField(max_length=8, default=generatebookingcode, unique=True, editable=False)

    def __str__(self):
        return self.booking_code

    def save(self, *args, **kwargs):
        if not self.booking_code:
            self.booking_code = generatebookingcode()
        super(RoomBooking, self).save(*args, **kwargs)
