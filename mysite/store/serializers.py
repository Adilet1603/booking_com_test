from .models import *
from rest_framework import serializers

class UserProfileserializers(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['username']

class Categoryserializers(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ImagesProductserializers(serializers.ModelSerializer):
    class Meta:
        model = ImagesProduct
        fields = '__all__'

class ProductListserializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['id','product_image','product_name','images_product','description','price','product_videos']

class ProductSimpleserializers(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ['product_name','product_image']

class ReviewSerializers(serializers.ModelSerializer):
    user = UserProfileserializers()

    class Meta:
        model = ReviewProduct
        fields = ['id','user','comment','created_at']

class Ratingserializers(serializers.ModelSerializer):
    client = UserProfileserializers()
    product = ProductSimpleserializers
    class Meta:
        model = Rating
        fields = ['id','client','stars']



class ProductDetailserializers(serializers.ModelSerializer):
    category = Categoryserializers()
    images_product = ImagesProductserializers(read_only=True,many=True)
    review_product = ReviewSerializers(read_only=True, many=True)
    rating_product = Ratingserializers(read_only=True,many=True)

    class Meta:
        model = Product
        fields = ['id','category','product_image','product_name',
                  'images_product','description','price','product_videos','review_product','rating_product']

class ReviewProductserializers(serializers.ModelSerializer):
    user = UserProfileserializers()
    product = ProductSimpleserializers
    class Meta:
        model = ReviewProduct
        fields = '__all__'

class Favoriteserializers(serializers.ModelSerializer):
    user = UserProfileserializers()

    class Meta:
        model = Favorite
        fields = ['id','user']

class FavoriteItemserializers(serializers.ModelSerializer):
    product = ProductListserializers()
    class Meta:
        model = FavoriteItem
        fields = ['id','favorite','product','like']

class FavoriteDetailserializers(serializers.ModelSerializer):
    user = UserProfileserializers()
    favorite_items = FavoriteItemserializers(read_only=True,many=True)

    class Meta:
        model = Favorite
        fields = ['id','user','favorite_items']


class CartItemserializers(serializers.ModelSerializer):

    class Meta:
        model = CartItem
        fields = ['product','quantity']

class Cartserializers(serializers.ModelSerializer):
    user =UserProfileserializers()
    items = CartItemserializers(read_only=True,many=True)
    class Meta:
        model = Cart
        fields =['id','user','items']

class Orderserializers(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class OrderItemserializers(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'
