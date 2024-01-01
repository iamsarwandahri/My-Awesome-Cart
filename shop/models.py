from django.db import models
from django.utils import timezone


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=100)
    category = models.CharField(max_length=50, default='')
    subcategory = models.CharField(max_length=50, default="")
    desc = models.TextField(default='')
    price = models.IntegerField(default="10")
    pub_date = models.DateTimeField(default=timezone.now())
    image = models.ImageField(upload_to='blog/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=50)
    desc = models.TextField(max_length=500)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.TextField()
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    address = models.CharField(blank=False, max_length=254)
    city = models.CharField(max_length=254)
    state = models.CharField(max_length=200)
    zip_code = models.IntegerField()
    phone = models.CharField(max_length=254)

    def __str__(self):
        return self.name


class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.CharField(max_length=100)
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."
