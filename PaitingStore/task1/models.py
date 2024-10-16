from django.db import models

# Create your models here.
class Buyer(models.Model):
    name = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=7, decimal_places=2)
    age = models.IntegerField()

    def __str__(self):
        return self.name


class Painting(models.Model):
    title = models.CharField(max_length=100)
    cost = models.DecimalField(max_digits=7, decimal_places=2)
    size = models.DecimalField(max_digits=7, decimal_places=2)  # GB
    description = models.TextField()
    age_limited = models.BooleanField(default=False)
    buyer = models.ManyToManyField(Buyer, related_name='buyers')

    def __str__(self):
        return f'{self.title} | {self.description}. Стоимость: {self.cost}'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.name} .Место проживания {self.city}'


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    customer = models.ManyToManyField(Customer, related_name='products')

    def __str__(self):
        return f'{self.title} | {self.description}. Стоимость: {self.cost}'
