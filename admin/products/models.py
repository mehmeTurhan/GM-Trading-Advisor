from django.db import models
from .util import fetch_stock_data_and_publish


class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    likes = models.PositiveIntegerField(default=0)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # Fetch stock data and publish to RabbitMQ exchange after saving a Product instance
        #fetch_stock_data_and_publish()

class User(models.Model):
    pass
