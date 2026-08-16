from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.
@admin.register(User)   
class CustomUserAdmin(UserAdmin):
    model = User
    ordering = ('phone_number',)
    list_display = ('phone_number', 'first_name', 'is_online', 'is_staff')
    list_filter = ('is_staff', 'is_active')
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Profile', {'fields': ('first_name', 'last_name', 'profile_picture', 'about')}),
        ('Status', {'fields': ('is_online', 'last_seen')}),
        ('Permissions', {'fields': ('is_active','is_staff', 'is_superuser', 'groups', 'user_permissions')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2')}
        ),
    )
    search_fields = ('phone_number',)
    