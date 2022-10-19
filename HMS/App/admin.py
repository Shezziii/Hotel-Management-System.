from django.contrib import admin
from .models import Hotel_Image , Booking  , Hotel , Amenities

# Register your models here.

admin.site.register(Hotel_Image )
admin.site.register( Booking )
admin.site.register( Hotel )
admin.site.register( Amenities)