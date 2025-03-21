from django.shortcuts import render 
from .models import Products
 
def product_list(request): 
    if not Products.objects.exists(): 
        Products.objects.create(p_name='FRock',quantity='2000',price='1200') 
        Products.objects.create(p_name='shirt',quantity='700',price='700') 
        Products.objects.create(p_name='Jeans',quantity='1000',price='150') 
        Products.objects.create(p_name='Hoodies',quantity='1200',price='1500') 
        Products.objects.create(p_name='sarees',quantity='800',price='5000') 
        Products.objects.create(p_name='kurti',quantity='2000',price='1850') 

    products = Products.objects.all() 
    return render(request, 'myapp/products.html', {'products': products})
