from asyncio.windows_events import NULL
from contextlib import nullcontext
from email import message
import email
from msvcrt import kbhit
from re import T, U
from turtle import pd
from unicodedata import name
from xml.etree.ElementTree import Comment
from django.forms import PasswordInput
from django.shortcuts import render,redirect
from pkg_resources import register_finder
from .models import *
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse
from django.contrib import messages
from datetime import datetime


def clear_list():
    avalible_slots.clear()
    non_avalible_slot.clear()

sdoctor=""
Date = datetime.today()
slots_list=["9:30 AM to 10 AM","10 AM to 10:30 AM","10:30 AM to 11 AM","1:00 PM to 1:30 PM","1:30 PM to 2 PM"]
avalible_slots=[]
non_avalible_slot=[]
def avoid_colsn(request):#Function for show only avalible Slots
    clear_list()
    if request.method == "POST":
        clear_list()
        global sdoctor
        global Date
        sdoctor = request.POST.get('sdoctor')
        Date = request.POST.get('date')
        for i in slots_list:
            # if( Apointment.objects.filter(date=request.POST.get('date')).exists() and Apointment.objects.filter(select_doctor=sdoctor).exists() and Apointment.objects.filter(slot=i).exists()):
            #     non_avalible_slot.append(i) 
            if(userRequest.objects.filter(Date=Date).filter(SelectDoctor=sdoctor).filter(Time=i)).exists():
                non_avalible_slot.append(i)      
            else:
                avalible_slots.append(i)  
    return render(request,'app/book_apt.html',{'no_slots':non_avalible_slot,'slots':avalible_slots})


# admininsert
def clear_list1():
    avalible_slots.clear()
    non_avalible_slot.clear()

sdoctor=""
Date = datetime.today()
slots_list=["9:30 AM to 10 AM","10 AM to 10:30 AM","10:30 AM to 11 AM","1:00 PM to 1:30 PM","1:30 PM to 2 PM"]
avalible_slots=[]
non_avalible_slot=[]
def avoid_colsn1(request):#Function for show only avalible Slots
    clear_list()
    if request.method == "POST":
        clear_list()
        global sdoctor
        global Date
        sdoctor = request.POST.get('sdoctor')
        Date = request.POST.get('date')
        for i in slots_list:
            # if( Apointment.objects.filter(date=request.POST.get('date')).exists() and Apointment.objects.filter(select_doctor=sdoctor).exists() and Apointment.objects.filter(slot=i).exists()):
            #     non_avalible_slot.append(i) 
            if(userRequest.objects.filter(Date=Date).filter(SelectDoctor=sdoctor).filter(Time=i)).exists():
                non_avalible_slot.append(i)      
            else:
                avalible_slots.append(i)  
    return render(request,'app/admin_book.html',{'no_slots':non_avalible_slot,'slots':avalible_slots})

def  HomePageView(request):
    return render(request,"app\home.html")

def AppointementPageView(request):
    return render(request,"app/book_apt.html")

def ContactUsPageView(request):
    return render(request,"app\contact_us.html") 

def AboutPageView(request):
    return render(request,"app/about.html")

def AdminHomePageView(request):
    return render(request,"app/AdminHome.html")

def AdminAppointementPageView(request):
    return render(request,"app/admin_book.html") 


def ApprovedPageView(request):
    return render(request,"app/Appreoved.html")    


    
    #     if apointments:
    #             messages.success(request, 'Your response is submitted we will inform you shortly')
    #             # return render(request,'app/home.html')
    #     #messages.success(request, 'massage sended to admins..!')
    #     avalible_slots.clear()
        
        
    #     return render(request,'app/book_apt.html')  
    # avalible_slots.clear()
    
    
    # return render(request,'app/home.html')


'''def InsertData(request):
    # Data come from html to view
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    address = request.POST['address']
    gender = request.POST['exampleRadios']
    contact = request.POST['contact']
    date = request.POST['date']
    time = request.POST['time']
    sdoctor = request.POST['sdoctor']
    comment = request.POST['comment']

    if (userRequest.objects.filter(Date=date).exists() and  userRequest.objects.filter(Time=time).exists() and userRequest.objects.filter(SelectDoctor=sdoctor).exists()):
            messages.warning(request, 'Please Choose Another Date Or Slot Or Doctor')
    else:
            apointments = userRequest(Firstname=fname,Lastname=lname,Email=email,Gender=gender,Address=address,
                                         Contact=contact,Date=date,Time=time,SelectDoctor=sdoctor,Comment=comment)
            apointments.save()
            if apointments:
                messages.success(request, 'massage sended to admins..!')

    return render(request,'app\home.html')'''
   

def InsertData(request):
    # Data come from html to view
    if request.method == "POST":
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        gender = request.POST.get('exampleRadios')
        contact = request.POST.get('contact')
        # date = request.POST.get('date')
        slot = request.POST.get('slot')
        # sdoctor = request.POST.get('sdoctor')
        comment = request.POST.get('comment')
        apointments = userRequest(Firstname=fname,Lastname=lname,Email=email,Gender=gender,Address=address,
                                         Contact=contact,Date=Date,Time=slot,SelectDoctor=sdoctor,Comment=comment)
        apointments.save()
        messages.success(request, 'Your response is submitted we will inform you shortly')
        clear_list()
        return render(request,'app/book_apt.html')  
    clear_list()
    return render(request,'app/home.html')


    # # creating object of model class
    # #inserting data into table
    # newuser = userRequest.objects.create(Firstname=fname,Lastname=lname,Email=email,Gender=gender,Address=address,
    #                                      Contact=contact,Date=date,Time=time,SelectDoctor=sdoctor,Comment=comment)

    # if newuser:
    #     message = "Your response is submitted we will inform you shortly"
    #     messages.success(request,message)


    # return render(request,"app\home.html")                                     



def LoginAdmin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        #checking the email id with db
        #user = adminDb.objects.get(Username=email)
        # if not user.Email:
        #     message = "User dose not exits"
        #     messages.success(request,message)
        if adminDb.objects.filter(Username=email).exists():
            user = adminDb.objects.get(Username=email)
            if user.Password == password:
                # request.session['Firstname'] = user.Firstname
                # request.session['Lastname'] = user.Lastname
                # request.session['Email'] = user.Email
                # return render(request,"app/table.html")
                return redirect("all_data")
            else:
                message = "Password dose not match"
                messages.success(request,message)
                return render(request,"app/home.html")
        else:
            message = "Invalid email "
            messages.success(request,message)
            return render(request,"app/home.html")
    # else:
    #     return render(request,"app/home.html")        


def Table_all(request):
    all =  userRequest.objects.all().order_by("Date")
    return render(request,"app/table.html",{"key1":all})

def EditPage(request,pk):
    #fetching of data of particular id
     get_data= userRequest.objects.get(id=pk) 
     return render(request,"app/edit.html",{'key2':get_data})


def UpdateData(request,pk):
    udata = userRequest.objects.get(id=pk)
    udata.Firstname = request.POST['fname']
    udata.Lastname = request.POST['lname']
    udata.Email = request.POST['email']
    udata.Address = request.POST['address']
    udata.Gender = request.POST['exampleRadios']
    udata.Contact = request.POST['contact']
    udata.Date = request.POST['date']
    udata.Time = request.POST['time']
    udata.SelectDoctor = request.POST['sdoctor']
    udata.Comment = request.POST['comment']
    #query for update
    udata.save()
    #render to show page
    return redirect('all_data')   




from django.template.loader import render_to_string
from django.core.mail import EmailMessage

def sendMail(request,pk):
    pdata = userRequest.objects.get(id=pk)
    templates = render_to_string('app/email_template.html',{'name':pdata.Firstname,"date":pdata.Date,"time":pdata.Time,"doctor":pdata.SelectDoctor,"id":pk})
    # d={{pdata.Date|pdata.Date:'dmy'}}
    # dt=str(d)
    appId = 22222+pdata.id
    fname = pdata.Firstname
    lname = pdata.Lastname
    email = pdata.Email
    gender = pdata.Gender
    address = pdata.Address
    contact = pdata.Contact
    date = pdata.Date
    time = pdata.Time
    sdoctor = pdata.SelectDoctor
    comment = pdata.Comment
    newuser = approvedReq.objects.create(AppointementId=appId,Firstname=fname,Lastname=lname,Email=email,Gender=gender,Address=address,
                                         Contact=contact,Date=date,Time=time,SelectDoctor=sdoctor,Comment=comment)

                                        
    email = EmailMessage(
        'Your Appointment at City Hospital is Confirmed',
        templates,
        settings.EMAIL_HOST_USER,
        [pdata.Email],
    )
    
    email.fail_silently=False
    email.send()
    # record = userRequest.objects.get(id = pk)
    # record.delete()

    
    text= """<h1>Email sent succesfully !</h1>"""
    #return HttpResponse(text)
    return redirect('all_data')

       



# def AdminInsertData(request):
#     if request.method == "POST":
#         fname = request.POST.get('fname')
#         lname = request.POST.get('lname')
#         email = request.POST.get('email')
#         address = request.POST.get('address')
#         gender = request.POST.get('exampleRadios')
#         contact = request.POST.get('contact')
#         # date = request.POST.get('date')
#         time = request.POST.get('slot')
#         # sdoctor = request.POST.get('sdoctor')
#         comment = request.POST.get('comment')
#         apointments = userRequest(Firstname=fname,Lastname=lname,Email=email,Gender=gender,Address=address,
#                                          Contact=contact,Date=date,Time=time,SelectDoctor=sdoctor,Comment=comment)
#         apointments.save()
#         if apointments:
#                 messages.success(request, 'Your response is submitted we will inform you shortly')
#         #messages.success(request, 'massage sended to admins..!')
#         avalible_slots.clear()
        
#         return render(request,'app/admin_book.html')  
#     avalible_slots.clear()
    
#     return render(request,'app/table.html')

def AdminInsertData(request):
    # Data come from html to view
    fname = request.POST['fname']
    lname = request.POST['lname']
    email = request.POST['email']
    address = request.POST['address']
    gender = request.POST['exampleRadios']
    contact = request.POST['contact']
    date = request.POST['date']
    time = request.POST['time']
    sdoctor = request.POST['sdoctor']
    comment = request.POST['comment']
    if (userRequest.objects.filter(Date=date).exists() and  userRequest.objects.filter(Time=time).exists() and userRequest.objects.filter(SelectDoctor=sdoctor).exists()):
            messages.warning(request, 'Please Choose Another Date Or Slot Or Doctor')
            #return HttpResponse("Please Chose Another Date Or Slot Or Doctor")
    else:
            apointments = userRequest(Firstname=fname,Lastname=lname,Email=email,Gender=gender,Address=address,
                                         Contact=contact,Date=date,Time=time,SelectDoctor=sdoctor,Comment=comment)
            apointments.save()
            if apointments:
                messages.success(request, 'Your response is submitted we will inform you shortly')



    # creating object of model class
    #inserting data into table
    # newuser = userRequest.objects.create(Firstname=fname,Lastname=lname,Email=email,Gender=gender,Address=address,
    #                                      Contact=contact,Date=date,Time=time,SelectDoctor=sdoctor,Comment=comment)

    # if apointments:
    #     message = "Your response is submitted we will inform you shortly"
    #     messages.success(request,message)                                     

    return render(request,"app/admin_book.html")

# importing the necessary libraries
from django.http import HttpResponse
from django.views.generic import View
from app import models
from .process import html_to_pdf 
from django.template.loader import render_to_string
from django.template.loader import get_template






class GeneratePDF1(View):
    def get(self, request,pk, *args, **kwargs):
        template = get_template('app/Pdf_template.html')
        pdata = userRequest.objects.get(id=pk)
        context = {'name':pdata.Firstname,
        "lname":pdata.Lastname,
        "date":pdata.Date,
        "time":pdata.Time,
        "doctor":pdata.SelectDoctor,
        "id":22222+pdata.id,
        }
            
        
        html = template.render(context)
        pdf = html_to_pdf('app/Pdf_template.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'Recipt.pdf'
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")



#Creating a class based view
class GeneratePDF(View):
    def get(self, request,pk, *args, **kwargs):
        template = get_template('app/Pdf_template.html')
        pdata = approvedReq.objects.get(id=pk)
        context = {'name':pdata.Firstname,
        "lname":pdata.Lastname,
        "date":pdata.Date,
        "time":pdata.Time,
        "doctor":pdata.SelectDoctor,
        "id":pdata.AppointementId,
        }
            
        
        html = template.render(context)
        pdf = html_to_pdf('app/Pdf_template.html', context)
        if pdf:
            response = HttpResponse(pdf, content_type='application/pdf')
            filename = 'Recipt.pdf'
            content = "inline; filename=%s" %(filename)
            download = request.GET.get("download")
            if download:
                content = "attachment; filename=%s" %(filename)
            response['Content-Disposition'] = content
            return response
        return HttpResponse("Not found")
        
            

def ApprovedData(request):
    if request.method == "POST":
        date=request.POST.get('date')
        if not date: #bagahycha ki date empth ahe ka?? te asel tar purna table display kara
            return render(request,'app/Appreoved.html',{'key3':approvedReq.objects.all()})  

        #check kara ki enter keleli date valid ahe ka kiva data base madhe present ahe ka
        elif approvedReq.objects.filter(Date=date).exists(): #Asel tar date specific DATA dakhava
            return render(request,'app/Appreoved.html',{'key3':approvedReq.objects.filter(Date=date)})

        else: #Nasel Tar Http error throw kara
            return HttpResponse("date not found")
   
    else:
        # Ani varil paki kahi nahi/ method post nasel tar Collect all records from table  and
        return render(request,'app/Appreoved.html',{'key3':approvedReq.objects.all()})            



def Done(request,pk):
    record = approvedReq.objects.get(id = pk)
    record.delete()
    return redirect('showtable')


