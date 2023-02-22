from django.contrib import admin
from user.models import Userdetails, Service, Breakdown, Feedback

# Register your models here.
admin.site.register(Userdetails)
admin.site.register(Service)
admin.site.register(Breakdown)
admin.site.register(Feedback)
