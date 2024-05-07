from django.shortcuts import render,redirect
from django.db.models import Q
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
@login_required(login_url='/login/')
def home(request):
    queryset = Students.objects.all()
    # if request.method == 'POST':
    if request.GET.get('search'):
        search = request.GET.get('search')
        queryset = queryset.filter(
            Q(name__icontains=search)|
            Q(roll_no__icontains = search)|
            Q(department__icontains = search)
            
            )
    context = {
        'student':queryset
    } 
    return render(request,'home.html',context)
# Create your views here.

@login_required(login_url='/login/')
def add(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        father_name = data.get('father_name')
        department = data.get('department')
        semister = data.get('semister')
        roll_no = data.get('roll_no')
        image = request.FILES.get('image')
        
        Students.objects.create(
            name = name,
            father_name = father_name,
            department = department,
            semister = semister,
            roll_no = roll_no,
            image = image
        )
        return redirect('/add/')
    return render(request,'add.html')

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, 'Invalid username!!')
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request,'Invalid passward!!')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/')
    return render(request,'login.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def signup(request):
    if request.method == 'POST':
        first_name = request.POST.get('frist_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        # confrim_password = request.POST.get('confrim_password')
        user = User.objects.filter(username=username)
        
        if user.exists():
            messages.info(request, 'User already exists')
            return redirect('/signup/')

        user = User.objects.create(
            first_name=first_name,
            last_name=last_name,
            username=username,
            
        )
        user.set_password(password)
        user.save()
        messages.info(request,"Account created successfully!!!")
        return redirect('/login/')
    return render(request, 'signup.html')
        

