from django.contrib import admin
from django.contrib.auth.models import User
from multihospital_app.models import Hospitalavail,HospitalDetail,HospitalRequest
# Register your models here.


@admin.register(HospitalDetail)
class HospitalDetailAdmin(admin.ModelAdmin):
    list_display = ('user', 'address','landmark', 'city', 'state', 'postal_code', 'phone_number', 'country')
    search_fields = ('user__username', 'city', 'state', 'postal_code')

@admin.register(Hospitalavail)
class HospitalAvailAdmin(admin.ModelAdmin):
    list_display = ('user',  'availability')
    search_fields = ('user__username',)

@admin.register(HospitalRequest)
class HospitalRequestAdmin(admin.ModelAdmin):
    list_display = ( 'status', 'date_created')
    search_fields = ('requester__username', )
    list_filter = ('status', 'date_created')

admin.site.unregister(User)  # Unregister the default User admin
@admin.register(User)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('username', 'email')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')