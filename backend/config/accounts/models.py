import uuid
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager
from django.db import models

# Create your models here.
class User(AbstractBaseUser, PermissionsMixin): 
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone_number = models.CharField(max_length=15, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100,blank=True)
    profile_picture = models.ImageField(upload_to='profiles/', blank=True, null=True)
    about = models.CharField(max_length=255, default='Realtime chatting app', blank=True)
    is_online = models.BooleanField(default=False)
    last_seen = models.DateTimeField(default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    

    def __str__(self):
        return self.phone_number