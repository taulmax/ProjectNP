from django.urls import path, include
from .views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', index, name='index'),
    path('category/<category_slug>/', product_in_category, name='product_in_category'),
    path('products/<int:id>/', product_detail, name='product_detail'),
    path('products/<int:id>/comment/', comment_create, name='comment_create'),
    path('products/<int:product_id>/comments/<int:id>/reply/', reply_create, name='reply_create'),
    

    path('api/', ApiRoot.as_view(), name=ApiRoot.name),
    path('api/product-categories/', ProductCategoryList.as_view(), name=ProductCategoryList.name),
    path('api/product-categories/<int:pk>/', ProductCategoryDetail.as_view(), name=ProductCategoryDetail.name),
    path('api/products/', ProductList.as_view(), name=ProductList.name),
    path('api/products/<int:pk>/', ProductDetail.as_view(), name=ProductDetail.name),
    path('api/comments', CommentList.as_view(),name=CommentList.name),
    path('api/comments/<int:pk>', CommentDetail.as_view(),name=CommentDetail.name),

]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
