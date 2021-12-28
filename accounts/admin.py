from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)

admin.site.register(Users)
admin.site.register(Nutritious)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
