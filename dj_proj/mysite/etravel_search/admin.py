from django.contrib import admin
from .models import Bus,Search

# Register your models here.

admin.site.register(Bus,name='Bus')
admin.site.register(Search,name='Search')

