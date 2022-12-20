from django.shortcuts import render
from store.models import Product

# Create your views here.
def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    message = 'I am sorry to inform you you cant order from the website for now, you can only order using whatsApp'
    context = {
        'message': message,
        'product': product,
    }
    return render(request, '404.html', context)