from rest_framework import serializers
from .models import ArticlesModel

class ArticleSerializer(serializers.ModelSerializer):
    '''
        Serializer for Articles
    '''
    class Meta:
        model=ArticlesModel
        fields='__all__'

