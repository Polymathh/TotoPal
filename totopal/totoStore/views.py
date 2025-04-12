from django.shortcuts import render
from .models import Product

# Create your views here.
def home(request):
    products = Product.objects.prefetch_related('media').all()
    
    # Pre-process each product's media for unique colors
    for product in products:
        used_colors = []
        for media in product.media.all():
            if media.color and media.color not in used_colors:
                used_colors.append(media.color)
        product.used_colors = used_colors
    
    return render(request, 'store/home.html', {'products': products})
