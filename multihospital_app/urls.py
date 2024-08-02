# myapp/urls.py
from django.urls import path
from django.contrib import admin
from multihospital_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home', views.home, name='home'),  
    path('register', views.register, name='register'), 
    path('logout',views.logout_page , name="logout"),   
    path('login', views.login, name='login'),  
    path('adminlogin', views.adminlogin, name='adminlogin'),  
    path('hospitalinfo',views.hospitalinfo , name="hospitalinfo"),   
    path('hospitalreq',views.hospitalreq , name="hospitalreq"),   
    path('allhospitalavail',views.allhospitalavail , name="allhospitalavail"),   
    path('hospitalhome', views.hospitalhome, name='hospitalhome'), 
    path('hospital_detail/create/', views.hospital_detail_create, name='hospital_detail_create'),
    path('hospital_detail/update/', views.hospital_detail_update, name='hospital_detail_update'), 
    path('hospital_detail/', views.hospital_detail_view, name='hospital_detail_view'),
    path('addhospitalavail', views.addhospitalavail, name='addhospitalavail'), 
    path('availabilityinfo', views.availabilityinfo, name='availabilityinfo'), 
    path('remove/<int:id>', views.remove, name='remove'), 
    path('adminremove/<int:id>', views.adminremove, name='adminremove'), 
    path('update/<int:id>', views.update, name='update'),
    path('adminupdate/<int:id>', views.adminupdate, name='adminupdate'),
    path('search', views.search, name='search'), 
    path('requestinfo', views.requestinfo, name='requestinfo'), 
    
    path('update', views.update, name='update'), 
    path('send_request/<int:hospital_avail_id>', views.send_request, name='send_request'),
    path('view_requests', views.view_requests, name='view_requests'),
    path('respond_to_request/<int:request_id>', views.respond_to_request, name='respond_to_request'),
    path('view_status/', views.view_status, name='view_status'), 
]
    
    

