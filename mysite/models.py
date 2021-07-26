from django.db import models
import django.utils.timezone as timezone
class Store(models.Model):
    store_name = models.CharField(max_length=100)
    store_number = models.CharField(max_length=20)
    # store_create_date = models.DateField(default=timezone.now)
    store_remake = models.CharField(max_length=20)
    def __str__(self):
        return str(self.store_name)
class dishes(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    dishes_name = models.CharField(max_length=50)
    dishes_price = models.FloatField(max_length=20)
    dishes_remake = models.CharField(max_length=10)
    def __str__(self):
        return str(self.dishes_name)
# Create your models here.
