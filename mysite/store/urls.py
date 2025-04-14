from django.urls import path, include
from .views import *
from rest_framework import routers
router = routers.SimpleRouter()

router.register( 'category', CategoryViewSet, basename= 'category')
router.register('ImagesProduct',ImagesProductViewSet,basename='ImagesProduct')
router.register('Order',OrderViewSet,basename='Order')
router.register('OrderItem',OrderItemViewSet,basename='OrderItem')


urlpatterns =[
    path('',include(router.urls)),
    path('product/',ProductViewSet.as_view(),name='product'),
    path('product/<int:pk>/',ProductDetailViewSet.as_view(),name='product_detail'),
    path('favorite_item/',FavoriteItemViewSet.as_view(),name='favorite_item-list'),
    path('favorite/',FavoriteViewSet.as_view(),name='favorite-list'),
    path('favorite/<int:pk>/',FavoriteRetrieveAPIVew.as_view(),name='favorite-detail'),

    path('rating/', RatingViewSet.as_view(), name='rating-list'),
    path('rating/<int:pk>/', RatingDetailViewSet.as_view(), name='rating-detail'),

    path('review/', ReviewViewSet.as_view(), name='review-list'),
    path('review/<int:pk>/', ReviewDetailViewSet.as_view(), name='review-detail'),

    path('cart/', CartViewSet.as_view(), name='cart-list'),

    path('cart_item/', CartItemViewSet.as_view(), name='cart_item-list'),
    path('cart_item/<int:pk>/', CartItemDetailViewSet.as_view(), name='cart_item-list'),
]