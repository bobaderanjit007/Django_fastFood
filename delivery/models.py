from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone

User = get_user_model()


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    city = models.CharField(max_length=100, blank=True)
    state = models.CharField(max_length=100, blank=True)
    zip_code = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.user.get_username()


class Products(models.Model):
    product = models.CharField(max_length=100)
    price = models.IntegerField()
    rating = models.FloatField()
    users = models.IntegerField()
    image = models.ImageField(upload_to='productImages/')

    def __str__(self):
        return self.product

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    id_user = models.IntegerField()
    id_product = models.IntegerField()

    def __str__(self):
        return self.user.get_username()



class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    phone = models.CharField(max_length=17, default=None)
    city = models.CharField(max_length=100, default=None)
    state = models.CharField(max_length=100, default=None)
    zip_code = models.CharField(max_length=100, default=None)
    item_count = models.IntegerField()
    item_price = models.IntegerField()
    total_price = models.IntegerField()
    order_date = models.DateField(default=timezone.now)
    rating = models.IntegerField(blank=True, default=0)

