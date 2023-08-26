from django.shortcuts import render,redirect
from Examapp.forms import *
from Examapp.models import *
from django.http import HttpResponse


# Create your views here.
def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        a=request.POST['fname']
        h=request.POST['lname']
        b=request.POST['uname']
        c=request.POST['password']
        d=request.POST['contact']
        e=request.POST['dob']
        f=request.POST['address']
        return redirect('stu/Login.html')
    return render(request,'stu/signup.html') 

def loginup(request):
    if request.method=='POST':
       b=request.POST['uname']
       c=request.POST['password']
    return render(request,'stu/login.html');

def signUp(request):
    try:
        if request.method=='POST':
            s=TeacherModel(request.POST)
            s.fname=request.POST['fname']
            s.lname=request.POST['lname']
            s.uname=request.POST['uname']
            s.password=request.POST['password']
            s.contact=request.POST['contact']
            s.save()
            return redirect('/teacher/Tlogin')
        else:
            reg=Signup()
            return render(request,'teacher/SignUP.html',{'reg':reg})
    except Exception as e:
        return HttpResponse(e)

def loginUP(request):
    if request.method=='POST':
        b=request.POST['uname']
        c=request.POST['password']
    return render(request,'teacher/login.html') 



def admin(request):
    if request.method=='POST':
        b=request.POST['uname']
        c=request.POST['password']
    return render(request,'admin.html') 

def contact(request):
    
    return render(request,'contact.html')

def tdashboard(request):
    
    return render(request,'teacher/dashboard.html')

def mcourse(request):
    
    return render(request,'teacher/mcourse.html')

def mquestion(request):
    
    return render(request,'teacher/mquestion.html')

def addexam(request):
    
    return render(request,'teacher/Tadd_exam.html')

def viewexam(request):
    
    return render(request,'teacher/Tview_exam.html')

def viewquestion(request):
    
    return render(request,'teacher/Tview_question.html')

def addquestion(request):
    
    return render(request,'teacher/Tadd_question.html')