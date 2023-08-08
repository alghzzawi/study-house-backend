from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
# Register your models here.

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = [
        "username",
        "email",
        "phone_number",
        "Is_employee",
    ]
    add_fieldsets=((
        'None',{
            'fields':('username','email','password','password2'),
        }
    ),(
        'personal information',{
            'fields':('phone_number','Is_employee'),
        }
    ),)

admin.site.register(CustomUser,CustomUserAdmin)