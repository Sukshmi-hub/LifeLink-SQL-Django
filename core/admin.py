from django.contrib import admin
from .models import User, Request, RedAlert

admin.site.register(User)
admin.site.register(Request)
admin.site.register(RedAlert)

# Register your models here.
