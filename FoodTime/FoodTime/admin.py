from django.contrib import admin

# Register your models here.
from .models import FoodItem,Registers,Feedback,Order

admin.site.register(FoodItem)

admin.site.register(Registers)

admin.site.register(Feedback)

admin.site.register(Order)