# myapp/views.py
from django.shortcuts import render,get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth import login as auth_login, authenticate,logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.db import DatabaseError
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm,CustomLoginForm,HospitalavailForm,HospitalAvailSearchForm,HospitalRequestForm,HospitalRequestResponseForm,HospitalDetailForm

from .models import Hospitalavail,HospitalRequest,HospitalDetail


def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()  
            messages.success(request,"Register Successfully and you can login...")      
            return redirect('login')  # Redirect to a home page or other success page
        else:
                messages.warning(request,'Password Mismatch...')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                auth_login(request, user)
                messages.success(request,'Login Successfully')
                return redirect('hospitalhome')  # Redirect to a home page or dashboard
            else:
                messages.error(request,'Invalid user name and password.')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

def adminlogin(request):    
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if username=='admin' and password=='admin':
            return redirect('hospitalinfo')
        else:
            messages.error(request,'Incorrect Username and Password.')   
        
        
    return render(request, 'admin/adminlogin.html')

def logout_page(request):
    if request.user.is_authenticated:
        logout(request)
        messages.success(request,'Logout Successfully')
    return redirect('/home')


def home(request):
    users = User.objects.all()
    return render(request, 'home.html',{'users': users})

def hospitalinfo(request):
    hospital_detail = HospitalDetail.objects.all()
    user=User.objects.all()

    return render(request, 'admin/hospitalinfo.html',{'hospital_detail':hospital_detail ,'user':user})

def hospitalreq(request):
    hospital=HospitalRequest.objects.all()

    return render(request, 'admin/hospitalreq.html',{'hospital':hospital})

def allhospitalavail(request):
    items = Hospitalavail.objects.all()
    return render(request, 'admin/allhospitalavail.html',{'items': items})


def hospitalhome(request):
    user = request.user
    try:
        hospital_detail = HospitalDetail.objects.get(user=request.user)
    except HospitalDetail.DoesNotExist:
        hospital_detail = None 
    return render(request, 'hospital/hospitalhome.html',{'hospital_detail': hospital_detail , 'user':user})

def hospital_detail_create(request):
    if request.method == 'POST':
        form = HospitalDetailForm(request.POST)
        if form.is_valid():
            hospital_detail = form.save(commit=False)
            hospital_detail.user = request.user
            hospital_detail.save()
            return redirect('hospitalhome')
    else:
        form = HospitalDetailForm()
    return render(request, 'hospital/hospitaldetails.html', {'form': form})



def hospital_detail_update(request):
    hospital_detail = get_object_or_404(HospitalDetail, user=request.user)
    if request.method == 'POST':
        form = HospitalDetailForm(request.POST, instance=hospital_detail)
        if form.is_valid():
            form.save()
            return redirect('hospitalhome')
    else:
        form = HospitalDetailForm(instance=hospital_detail)
    return render(request, 'hospital/hospitalupdate.html', {'form': form})

def hospital_detail_view(request):
    hospital_detail = get_object_or_404(HospitalDetail, user=request.user)
    return render(request, 'hospital/hospitalhome.html', {'hospital_detail': hospital_detail})

def addhospitalavail(request):
    if request.method == 'POST':
        form = HospitalavailForm(request.POST,request.FILES)
        if form.is_valid():
            
            hospital_avail = form.save(commit=False)
            hospital_avail.user = request.user
            hospital_avail.save()
            
            return redirect('availabilityinfo')
        else:
            messages.success(request,'error')
    else:
        form = HospitalavailForm()
        
    return render(request, 'hospital/addhospitalavail.html',{'form': form})

def availabilityinfo(request):
    items = Hospitalavail.objects.filter(user=request.user)
    return render(request, 'hospital/availabilityinfo.html',{'items': items})

def remove(request, id):
    hospital_avail = get_object_or_404(Hospitalavail, id=id)
    if request.method == 'POST':
        hospital_avail.delete()
        messages.success(request,'Remove Successfully...')
        return redirect('availabilityinfo')
    return render(request, 'hospital/remove.html', {'hospital_avail': hospital_avail})

def adminremove(request, id):
    hospital_avail = get_object_or_404(Hospitalavail, id=id)
    if request.method == 'POST':
        hospital_avail.delete()
        messages.success(request,'Remove Successfully...')
        return redirect('allhospitalavail')
    return render(request, 'admin/remove.html', {'hospital_avail': hospital_avail})
    

def search(request):
    search_form = HospitalAvailSearchForm(request.GET)
    query = request.GET.get('query')
    hospital_avails = Hospitalavail.objects.exclude(user=request.user)
    if query:
        hospital_avails = Hospitalavail.objects.filter( name__icontains=query)
    return render(request, 'hospital/search.html', {'hospital_avails': hospital_avails, 'search_form': search_form})

def requestinfo(request):
    return render(request, 'hospital/requestinfo.html')

def update(request,id):
    hospital_avail = get_object_or_404(Hospitalavail, id=id)
    if request.method == 'POST':
        form = HospitalavailForm(request.POST, request.FILES, instance=hospital_avail)
        if form.is_valid():
            form.save()
            return redirect('availabilityinfo')
    else:
        form = HospitalavailForm(instance=hospital_avail)
    return render(request, 'hospital/update.html', {'form': form, 'update': True})

def adminupdate(request,id):
    hospital_avail = get_object_or_404(Hospitalavail, id=id)
    if request.method == 'POST':
        form = HospitalavailForm(request.POST, request.FILES, instance=hospital_avail)
        if form.is_valid():
            form.save()
            return redirect('allhospitalavail')
    else:
        form = HospitalavailForm(instance=hospital_avail)
    return render(request, 'admin/update.html', {'form': form, 'update': True})
   
def send_request(request, hospital_avail_id):
    hospital_avail = get_object_or_404(Hospitalavail, id=hospital_avail_id)
    if request.method == 'POST':
        form = HospitalRequestForm(request.POST)
        if form.is_valid():
            hospital_request = form.save(commit=False)
            hospital_request.from_user = request.user
            hospital_request.to_user = hospital_avail.user
            hospital_request.hospital_avail = hospital_avail
            hospital_request.save()
            return redirect('view_status')
    else:
        form = HospitalRequestForm()
    return render(request, 'hospital/send_request.html', {'form': form, 'hospital_avail': hospital_avail})


def view_requests(request):
    # received_requests = request.user.received_requests.filter(status='pending')
    # return render(request, 'hospital/view_requests.html', {'received_requests': received_requests})
    sent_requests = request.user.sent_requests.all()
    received_requests = request.user.received_requests.all()

    context = {
        'sent_requests': sent_requests,
        'received_requests': received_requests,
    }
    return render(request, 'hospital/view_requests.html', context)


def respond_to_request(request, request_id):
    hospital_request = get_object_or_404(HospitalRequest, id=request_id)
    if request.method == 'POST':
        form = HospitalRequestResponseForm(request.POST, instance=hospital_request)
        if form.is_valid():
            form.save()
            return redirect('view_requests')
    else:
        form = HospitalRequestResponseForm(instance=hospital_request)
    return render(request, 'hospital/respond_to_request.html', {'form': form, 'hospital_request': hospital_request})

def view_status(request):
    sent_requests = request.user.sent_requests.all()
    received_requests = request.user.received_requests.all()

    context = {
        'sent_requests': sent_requests,
        'received_requests': received_requests,
    }
    return render(request, 'hospital/view_status.html', context)