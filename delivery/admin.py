from django.contrib import admin
from .models import Profile, Products, Cart, Orders

admin.site.register(Profile)
admin.site.register(Products)
admin.site.register(Cart)
admin.site.register(Orders)