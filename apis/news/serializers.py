from rest_framework import serializers
from apis.news.models import News, NewsComment

# class NewsSerializer(serializers.Serializer):
#     title = serializers.CharField(max_length=200)
#     content = serializers.CharField()
#     reported_at = serializers.CharField(max_length=30, required= False)
#     avatar = serializers.ImageField(required= False)
#     author = serializers.PKOnlyObject()


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = ('title','content','author','category')
