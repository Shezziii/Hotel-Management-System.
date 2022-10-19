from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.
class Base(models.Model):
      id=models.UUIDField(default=uuid.uuid4 , primary_key=True)
      created_at=models.DateTimeField(auto_now_add=True)      
      updated_at=models.DateTimeField(auto_now_add=True)
      class meta:
            abstract=True

class Amenities(Base):
      Amenities_name=models.CharField(max_length=50)
      def __str__(self):
            return self.Amenities_name
            
class Hotel(Base):
      Hotel_name=models.CharField(max_length=50)
      description=models.TextField()
      cost=models.IntegerField()
      place=models.CharField(max_length=50)
      amenities = models.ManyToManyField(Amenities)
      room_count = models.IntegerField(default=10)
      def __str__(self):
             return self.Hotel_name
      
class Hotel_Image(models.Model):
       hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
       images=models.ImageField(upload_to='images')       
       
class Booking(models.Model):
      hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE)
      user=models.ForeignKey(User,on_delete=models.CASCADE)
      CheckIn=models.DateField()
      CheckOut=models.DateField()
      room_booked=models.IntegerField(default=1)
      Type=models.CharField(max_length=50,choices=(('Pre Paid' , 'Pre Paid') , ("Post Paid" , 'Post Paid') ))
      def __str__(self):
             return f'{self.CheckIn} - {self.CheckOut}'       