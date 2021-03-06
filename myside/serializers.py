
from .models import Category
from .models import Product
from .models import Comment
from .models import Reply
from rest_framework import serializers


class ProductCategorySerializer(serializers.ModelSerializer):
    products = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='product-detail'
    )
    class Meta:
        model = Category
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    replies = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='reply-detail'
    )
    
    class Meta:
        model = Comment
        fields = '__all__'

class ReplySerializer(serializers.ModelSerializer):
    class Meta:
        model = Reply
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    comments = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='comment-detail'
    )
    class Meta:
        model = Product
        fields = ('name',
                'category',
                'img',
                'brand',
                'description',
                'price',
                'stock',
                'comments')
