from django.contrib import admin
from .models import Order,Profile
# Register your models here.
admin.site.register([Profile,Order])