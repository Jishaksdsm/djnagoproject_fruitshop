from django.db import models
from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()
# Create your models here.

class Fruit(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='fruits/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
    


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fruit = models.ForeignKey(Fruit, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.user.username}'s cart - {self.fruit.name}"