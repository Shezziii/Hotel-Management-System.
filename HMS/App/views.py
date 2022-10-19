from django.shortcuts import render , HttpResponseRedirect , redirect
from django.http import HttpResponse
from django.db.models import Q
from .models import Hotel_Image , Booking  , Hotel , Amenities
from django.contrib.auth.models import User
from django.contrib.auth import login , logout , authenticate
from django.contrib import messages
from .decorater import is_authenticate


# Create your views here.
def home(request):
      hotels_objs=Hotel.objects.all()
      amenities_objs=Amenities.objects.all()
      context={ 'hotels_objs' : hotels_objs , 'amenities_objs' : amenities_objs}
      if request.method=='POST':
            sort_by=request.POST['sort_by'] 
            search=request.POST['search'] 
            amenities=request.POST.getlist('amenities') 
            print(amenities)
            if sort_by:
                  if sort_by == 'ASC':
                        hotels_objs = hotels_objs.order_by('cost')
                  elif sort_by == 'DSC':
                        hotels_objs = hotels_objs.order_by('-cost')
            if search:
                  hotels_objs = hotels_objs.filter(
                        Q(Hotel_name__icontains = search) |
                        Q(description__icontains = search) )
            if len(amenities):
                  hotels_objs = hotels_objs.filter(amenities__Amenities_name__in = amenities).distinct()
            context = {'amenities_objs' : amenities_objs , 'hotels_objs' : hotels_objs , 'sort_by' : sort_by , 'search' : search , 'amenities' : amenities}          
      return render(request,"home.html",context)
      
      
def details(request,id):
      hotels_obj=Hotel.objects.get(id=id)
      if request.method == "POST":
          CheckIn = request.POST.get('checkin')
          CheckOut = request.POST.get('checkout')
          print(request.user)
          if CheckIn>CheckOut:
              messages.error(request,'Please Provide Valid Dates.')
          if availability(CheckIn,CheckOut,id):
              hotels_obj=Hotel.objects.get(id=id)
              Booking(user=request.user,hotel=hotels_obj,CheckIn=CheckIn,CheckOut=CheckOut,Type='Post Paid').save()
              messages.success(request,'Hotel is Booked Successfully.')
          else:
              messages.error(request,'Hotel is already Booked in these Dates.')     
      return render(request, "details.html" , { 'hotels_obj' : hotels_obj}) 
  
@is_authenticate          
def loginView(request):
    if request.method=="POST":
        name=request.POST.get('uname')
        password=request.POST.get('upass')
        if user:=authenticate(username=name,password=password):
            login(request,user)
            return redirect('home')
        else:
            messages.error(request,"Invalid Username and Password.")    
    return render(request,'login.html')
    
@is_authenticate    
def SignupView(request):
    if request.method=="POST":
        name=request.POST.get('uname')
        email=request.POST.get('uemail')
        password=request.POST.get('upass')
        Cpass=request.POST.get('cpass')
        
        if User.objects.filter(email=email):
            messages.error(request,"This email is already Taken.")
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        if password!=Cpass:
            messages.error(request,'Password is Not match.')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        user=User(username=name,email=email,password=password)
        user.save()
        login(request,user)
        
        return redirect('home')
    return render(request,'register.html') 

   
def LogoutView(request):
    logout(request)
    return redirect('login')

              

#all the Logic is Here.

def availability(CheckIn,CheckOut,hotel_id):
    hotel=Hotel.objects.get(id=hotel_id)
    # case 1: a room is booked before the CheckIn date, and checks out after the requested CheckIn date
    case_1 = Booking.objects.filter(hotel=hotel, CheckIn__lte=CheckIn, CheckOut__gte=CheckIn).exists()

    # case 2: a room is booked before the requested CheckOut date and check_out date is after requested check_out date
    case_2 = Booking.objects.filter(hotel=hotel, CheckIn__lte=CheckOut, CheckOut__gte=CheckOut).exists()
            
    case_3 = Booking.objects.filter(hotel=hotel, CheckIn__gte=CheckIn, CheckOut__lte=CheckOut).exists()
    if case_1 or case_2 or case_3:
        return False
    return True                  
                                                       