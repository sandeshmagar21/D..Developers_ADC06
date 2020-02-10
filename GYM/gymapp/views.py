from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.http import HttpResponse, Http404

from django.db.models import Q
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.contrib import auth
from django.contrib.auth.models import Permission, User


from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required

from .forms import GymCreate, TrainerForm, AbcForm, MemberForm, PaymentForm, ContatForm
from gymapp.models import Gym, Trainer, Members, abc, Payment


#CRUD Operation
#Read
def index(request):
    shelf = Gym.objects.all()
    return render(request, 'gymapp/CRUD/premium.htm', {'shelf': shelf})

# Upload/Create    
def upload(request):
    upload = GymCreate()
    if request.method == 'POST':
        upload = GymCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("Invalid!!")
    else:
        return render(request, 'gymapp/CRUD/upload_form.htm', {'upload_form':upload})

# Update          
def update_form(request, gym_id):
    gym_id = int(gym_id)
    try:
        values = Gym.objects.get(id = gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    gym_form = GymCreate(request.POST or None, instance = values)
    if gym_form.is_valid():
       gym_form.save()
       return redirect('index')
    return render(request, 'gymapp/CRUD/upload_form.htm', {'upload_form':gym_form})

#Delete
def delete_form(request, gym_id):
    gym_id = int(gym_id)
    try:
        values = Gym.objects.get(id = gym_id)
    except Gym.DoesNotExist:
        return redirect('index')
    values.delete()
    return redirect('index')



"""
Search Functionality
"""
def search_function_hai(request):
    if request.method =='GET':
        finds = request.GET['hacsac']
        if finds:
            match = Gym.objects.filter(Q(workoutname__icontains=finds))                             
            if match:                
                return render(request,'gymapp/CRUD/premium.htm', {'sac':match})
            else:
                messages.error(request, "The word, You type did  not Exist")
        else:
            return HttpResponseRedict('gymapp/CRUD/premium.htm')  
    return render(request, 'gymapp/CRUD/premium.htm')         


#For Registration Page
def view_register_users(request):
    if request.method =="GET":
        return render(request,'Registration/signup.htm')
    else:
        user = User.objects.create_user(username=request.POST['username'],password=request.POST['password'],email=request.POST['email'])
        user.save()
        return render(request,'login/home.htm')
        return HttpResponse("Signup Successful")
        return redirect('/')

# For Login Page
def view_authenticate_users(request):
    if request.method =="GET":
            return render (request,'Login/login.htm')
    else:
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            login(request,user)
            return render(request,"additionalhtml/access.htm")
        else:
            html = '<html> <body background-color="pink"> <h1> UserName or Password is Invalid!! </h1><input type="button" value="Go Back" onclick="history.go(-1)"> </body></html>'    
            return HttpResponse(html)

#Logout Page
def logout(request):
    auth.logout(request)   
    return render(request,'login/login.htm')

#Authorized Page which unauthorized user doesnot able view 
def view_accesspage_by_authorized_user(request):
    if request.user.is_authenticated:
        return render(request, "additionalhtml/access.htm")
    else:
        return HttpResponse("Error, Please Register First!!!")


def contact(request):
    return render(request,'gymapp/Navbar/contact.htm')      


def home(request):
  return render(request,'login/home.htm')

def course(request):
    return render(request,'gymapp/NavBar/course.htm')

def singuppage(request):
    return render(request,'registration/signup.htm')

def accesspage(request):
    return render(request,'additionalhtml/access.htm')

def schedulepage(request):
    return render(request,'gymapp/NavBar/schedule.htm')

def trainderdet(request):
    return render(request,'gymapp/NavBar/trainerdet.htm')

# view function for trainer where trainer can register their name
def trainer_create_form(request):
    if request.method =='POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            sav = form.save() 
        html = '<html> <body style="color: black; background-color:rgba(133, 126, 126, 0.479);"> <h1> Data is Successfully Saved </h1><input type="button" value="Go Back" onclick="history.go(-1)"> </body></html>'    
        return HttpResponse(html)   
    else:
        form = TrainerForm()  
        return render(request, 'gymapp/Model/trainer.htm', {'form': form}) 

# view function for course where trainer can upload their course
def abc_create_form(request):
    if request.method =='POST':
        form1 = AbcForm(request.POST, request.FILES)
        if form1.is_valid():
            store = form1.save()
        html = '<html> <body style="color: black; background-color:rgba(133, 126, 126, 0.479);"> <h1> Data is Successfully Saved </h1><input type="button" value="Go Back" onclick="history.go(-1)"> </body></html>'    
        return HttpResponse(html)    
    else:
        form1 = AbcForm()  
        return render(request, 'gymapp/Model/abc.htm', {'form': form1}) 

# view function for payment where they can pay for course
def contract_create_form(request):
    if request.method =='POST':
        feedback = ContatForm(request.POST)
        if feedback.is_valid():
            store = feedback.save()
        html = '<html> <body style="color: black; background-color:rgba(133, 126, 126, 0.479);"> <h1> Thank you for your Feedback !! </h1><input type="button" value="Go Back" onclick="history.go(-1)"> </body></html>'    
        return HttpResponse(html)    
    else:
        feedbac=  ContatForm()  
        return render(request, 'gymapp/NavBar/contact.htm', {'contact': feedbac}) 
        
# view function for payment where they can pay for course
def payment_create_form(request):
    if request.method =='POST':
        form2 = PaymentForm(request.POST)
        if form2.is_valid():
            save = form2.save()
        html = '<html> <body background-color="pink"> <h1> Data is Successfully Saved </h1><input type="button" value="Go Back" onclick="history.go(-1)"> </body></html>'    
        return HttpResponse(html)     
    else:
        form2 = PaymentForm()  
        return render(request, 'gymapp/Model/payment.htm', {'recorded': form2})   


# view function for member where user can register their name as member
def members_create_form(request):
    if request.method =='POST':
        form2 = MemberForm(request.POST)
        if form2.is_valid():
            save = form2.save()
        html = '<html> <body style="color: black; background-color:rgba(133, 126, 126, 0.479);"> <h1> Data is Successfully Saved </h1><input type="button" value="Go Back" onclick="history.go(-1)"> </body></html>'    
        return HttpResponse(html)     
    else:
        form2 = MemberForm()  
        return render(request, 'gymapp/Model/members.htm', {'savedhai': form2})

# view function of course which is uploaded by trainer         
def view_all_course_uploaded_by_trainer(request):
    list_of_courses = abc.objects.all()
    context_store = {
        'store':list_of_courses
    } 
    return render(request, "gymapp/NavBar/listcourse.htm", context_store )                

