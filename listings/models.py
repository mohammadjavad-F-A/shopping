from django.db import models
from main.models import product
from django.core.validators import MaxValueValidator, MinValueValidator
from django.contrib.auth.models import User

class special_products(models.Model):
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    is_published = models.BooleanField(default=False)
    def __str__(self):
        return self.title


class comment(models.Model):
    product = models.IntegerField()
    user_name = models.CharField(max_length=40)
    content = models.TextField()
    cread_at = models.DateTimeField(auto_now_add=True)
    star = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return self.user_name


class address(models.Model):
    user_name = models.CharField(blank=True)
    user_id = models.IntegerField(blank=True)
    city = models.CharField(blank=True)
    district = models.CharField(blank=True)
    street = models.CharField(blank=True)
    alley = models.CharField(blank=True)
    plaque = models.IntegerField(blank=True)
    floor = models.IntegerField(blank=True)
    unit = models.IntegerField(blank=True)
    postal = models.IntegerField(blank=True)

    def __str__(self):
        return self.user_name

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return str(self.user)

class Order(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(blank=True)
    district = models.CharField(blank=True)
    street = models.CharField(blank=True)
    alley = models.CharField(blank=True)
    plaque = models.IntegerField(blank=True)
    floor = models.IntegerField(blank=True)
    unit = models.IntegerField(blank=True)
    postal = models.IntegerField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return str(self.user)

class OrderItem(models.Model):
    STATUS_CHOICES = (
        ('Pending', 'درحال بررسی'),
        ('confirmed', 'تایید شده'),
        ('shipped', "ارسال شده"),
        ('delivered', "تحویل داده شده")
    )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    delivered_at = models.DateTimeField(null=True, blank=True)
    expire_at = models.DateTimeField(null=True, blank=True)

    def mark_as_delivered(self):
        from django.utils import timezone
        from datetime import timedelta
        self.delivered_at = timezone.now()
        self.expire_at = timezone.now() + timedelta(hours=1)
        self.status = 'delivered'
        self.save()
    def __str__(self):
        return str(self.order)
