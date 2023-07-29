from django.contrib import admin
from .models import Department, Students_here

# Register your models here.
admin.site.register(Students_here)
admin.site.register(Department)