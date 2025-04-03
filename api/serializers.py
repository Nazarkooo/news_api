from rest_framework import serializers

from api.models import NewsType, NewsItem


class NewsTypeSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = NewsType
        fields = ('name', 'color')


class NewsItemSerializer(serializers.ModelSerializer):
    news_type_name = serializers.CharField(source='news_type.name')
    news_type_color = serializers.CharField(source='news_type.color')
    class Meta:
        model = NewsItem
        fields = ('title', 'about', 'description', 'news_type_name', 'news_type_color')

    def create(self, validated_data):
        news_type_name = validated_data.pop('news_type')['name']
        news_type = NewsType.objects.get(name=news_type_name)
        news_item = NewsItem.objects.create(news_type=news_type, **validated_data)
        return news_item
    
    def update(self, instance, validated_data):
        news_type_name = validated_data.pop('news_type')['name']
        news_type = NewsType.objects.get(name=news_type_name)
        
        instance.title = validated_data['title']
        instance.about = validated_data['about']
        instance.description = validated_data['description']
        instance.news_type = news_type
        
        instance.save()
        
        return instance


