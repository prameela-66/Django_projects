from django.db import models
class Products(models.Model):
    p_name=models.CharField(max_length=100)
    quantity=models.IntegerField()
    price=models.DecimalField(max_digits=10, decimal_places=2)
