from django.db import models
from django.contrib.auth.models import User


class UserAuthentication(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)


class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=255, null=True, blank=True)
    surname = models.CharField(max_length=255, null=True, blank=True)


# class Category(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#
#     def __str__(self):
#         return self.name+" candy"

class Category(models.Model):
    CHOCOLATE = 'Chocolate Candy'
    COTTON_CANDY = 'Cotton Candy'
    CHEWING_GUM = 'Chewing Gum'
    LOLLIPOP = 'Lollipop'
    HARD_CANDY = 'Hard Candy'
    GUMMY_CANDY = 'Gummy Candy'
    # Add more category choices if needed

    CATEGORY_CHOICES = [
        (CHOCOLATE, 'Chocolate Candy'),
        (COTTON_CANDY, 'Cotton Candy'),
        (CHEWING_GUM, 'Chewing Gum'),
        (LOLLIPOP, 'Lollipop'),
        (HARD_CANDY, 'Hard Candy'),
        (GUMMY_CANDY, 'Gummy Candy')
        # Add more choices if needed
    ]

    name = models.CharField(max_length=50, choices=CATEGORY_CHOICES)
    description = models.TextField()

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    in_Stocked = models.PositiveIntegerField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images/', null=True, blank=True)
    ingredients = models.TextField(null=True, blank=True)


# class ProductCategory(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     category = models.ForeignKey(Category, on_delete=models.CASCADE)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(null=True, blank=True)


class Order(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    card_number = models.CharField(max_length=16)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
