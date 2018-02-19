from django.contrib import admin
from .models import Bus,Search,Cost

# Register your models here.

admin.site.register(Bus,name='Bus')
admin.site.register(Search,name='Search')
admin.site.register(Cost,name='Cost')
