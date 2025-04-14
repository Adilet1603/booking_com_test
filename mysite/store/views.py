from rest_framework import viewsets, generics, permissions
from .serializers import *
from .models import *
from rest_framework.filters import SearchFilter,OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from .filters import ProductFilter
from .pagination import ProductPagination,RatingPagination
from .permissions import RatingCheck,ReviewCheck


class UserProfile(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileserializers

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = Categoryserializers

class ProductViewSet(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductListserializers
    filter_backends = [DjangoFilterBackend,SearchFilter,OrderingFilter]
    search_filter = ['product_name']
    ordering_fields = ['price']
    filterset_class = ProductFilter
    pagination_class = ProductPagination
    permission_classes = [permissions.IsAuthenticated]


class ProductDetailViewSet(generics.RetrieveAPIView):
    queryset = Product.objects.all()

class ImagesProductViewSet(viewsets.ModelViewSet):
    queryset = ImagesProduct.objects.all()
    serializer_class = ImagesProductserializers

class ReviewViewSet(generics.ListCreateAPIView):
    queryset = ReviewProduct.objects.all()
    serializer_class = ReviewProductserializers

class ReviewDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = ReviewProduct.objects.all()
    serializer_class = ReviewProductserializers
    permission_classes = [ReviewCheck]

class RatingViewSet(generics.ListCreateAPIView):
    queryset = Rating.objects.all()
    serializer_class = Ratingserializers
    pagination_class = RatingPagination
    permission_classes = [permissions.IsAuthenticated]

class RatingDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    serializer_class = Ratingserializers
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,RatingCheck]

class FavoriteViewSet(generics.ListAPIView):
    queryset = Favorite.objects.all()
    serializer_class = Favoriteserializers

class FavoriteRetrieveAPIVew(generics.RetrieveAPIView):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteDetailserializers

class FavoriteItemViewSet(generics.ListAPIView):
    queryset = FavoriteItem.objects.all()
    serializer_class = FavoriteItemserializers


class CartViewSet(generics.ListAPIView):
    serializer_class = Cartserializers

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

class CartItemViewSet(generics.ListCreateAPIView):
    serializer_class = CartItemserializers

    def get_queryset(self):
        return CartItem.objecrs.filter(cart__user=self.request.user)

    def perform_create(self, serializer):
        cart, create = Cart.object.get_or_create(user=self.request.user)
        serializer.save(cart=cart)


class CartItemDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    queryset = CartItem.objects.all()
    serializer_class = CartItemserializers

class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = Orderserializers

class OrderItemViewSet(viewsets.ModelViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemserializers










