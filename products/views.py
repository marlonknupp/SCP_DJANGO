from django.shortcuts import render
from products.models import product

def product_view(request):
    products = product.objects.all()
    return render(
        request=request,
        template_name='products.html',
        context={'products': products},
    ) 


