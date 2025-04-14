from django.contrib.auth.models import AbstractUser
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class UserProfile(AbstractUser):
    age = models.PositiveSmallIntegerField(null=True, blank=True)
    phone_number = PhoneNumberField(null=True,blank=True)
    profile_image = models.ImageField(upload_to='profile_image')
    date_registered = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.username



class Category(models.Model):
    category_name = models.CharField(max_length=64)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=32)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product_image = models.ImageField(upload_to='product_image')
    product_videos = models.FileField(upload_to='product_videos', null=True,blank=True)

    def __str__(self):
        return self.product_name


class ImagesProduct(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='images_product')
    images_product = models.ImageField(upload_to='images_product')

    def __str__(self):
        return f'{self.product}'


class ReviewProduct(models .Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='review_product')
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='rating_product')
    client = models.OneToOneField(UserProfile, on_delete=models.CASCADE)
    stars = models.IntegerField(choices=[(i, str(i)) for i in range(1,6)], verbose_name='Рейтинг')


class Favorite(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class FavoriteItem(models.Model) :
    favorite = models.ForeignKey(Favorite, on_delete=models.CASCADE,related_name='favorite_items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)

class Cart(models.Model) :
    user = models.OneToOneField(UserProfile,on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user}'

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(default=1)

    def __str__(self):
        return f'{self.cart}:{self.product}:{self.quantity}'

class Order(models.Model):
    user = models.OneToOneField(UserProfile, on_delete=models.CASCADE)

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=34)
    last_name = models.CharField(max_length=34)
    gmail = models.EmailField()
    phone_number = PhoneNumberField()
    address = models.TextField
    comment = models.TextField(null=True, blank=True)
    check_order = models.FileField
