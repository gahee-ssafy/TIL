from rest_framework import serializers
from .models import Article

# 홈페이지에서 쓰기에 필요없는 필드는 안쓴다. 
class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        # 직렬화 필드 
        fields = (
            'id',
            'title',
            'content',
        )