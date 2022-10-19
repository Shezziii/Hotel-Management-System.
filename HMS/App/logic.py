
#all the Logic is Here.

def availability(CheckIn,CheckOut,hotel_id):
    hotel=Hotel.objects.get(id=hotel_id)
    # case 1: a room is booked before the CheckIn date, and checks out after the requested CheckIn date
    case_1 = Booking.objects.filter(hotel=hotel, CheckIn__lte=CheckIn, CheckOut__gte=CheckIn).exists()

    # case 2: a room is booked before the requested CheckOut date and check_out date is after requested check_out date
    case_2 = Reservation.objects.filter(hotel=hotel, CheckIn__lte=CheckOut, CheckOut__gte=CheckOut).exists()
            
    case_3 = Reservation.objects.filter(hotel=hotel, CheckIn__gte=CheckIn, CheckOut__lte=CheckOut).exists()
    if case_1 or case_2 or case_3:
        return False
    return True                  
             