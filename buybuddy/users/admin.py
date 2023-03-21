from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class CustomUserAdmin(UserAdmin):
    add_form:
    form =
    model = 
    list_display = ['email', 'username']

    admin.site.register(CustomUserAdmin)
    

