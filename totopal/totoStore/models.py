from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    main_image = models.ImageField(upload_to='products/main_images/', blank=True, null=True)

    def __str__(self):
        return self.name
    
class ProductMedia(models.Model):
    MEDIA_TYPES = (
        ('image', 'Image'),
        ('video', 'Video'),
    )

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='media')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default='image')
    image = models.ImageField(upload_to='products/images', blank=True, null=True)
    video = models.FileField(upload_to='products/videos', blank=True, null=True)

    def __str__(self):
        return f'{self.product.name} Media ({self.media_type})'
