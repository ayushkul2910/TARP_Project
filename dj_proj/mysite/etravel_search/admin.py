from django.contrib import admin
from .models import Bus,Search,User_Journey

# Register your models here.

admin.site.register(Bus,name='Bus')
admin.site.register(Search,name='Search')
admin.site.register(User_Journey,name='User_Journey')

