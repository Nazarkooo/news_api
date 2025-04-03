from django.shortcuts import get_object_or_404

from rest_framework import status, permissions
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from .models import NewsType, NewsItem
from .serializers import NewsTypeSerializer, NewsItemSerializer


class NewsTypesViewset(ViewSet):
    permission_classes = [permissions.AllowAny]
    
    def list(self, request):
        news_types_qs = NewsType.objects.all()
        news_types_serializer = NewsTypeSerializer(news_types_qs, many=True)
        return Response(news_types_serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        news_type = get_object_or_404(NewsType, id=pk)
        news_type_serializer = NewsTypeSerializer(news_type)
        return Response(news_type_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        news_type_serializer = NewsTypeSerializer(data=request.data)
        news_type_serializer.is_valid(raise_exception=True)
        news_type_serializer.save()
        return Response({"status": "news type has been created"}, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        news_type = get_object_or_404(NewsType, id=pk)
        news_type_serializer = NewsTypeSerializer(instance=news_type, data=request.data)
        news_type_serializer.is_valid(raise_exception=True)
        news_type_serializer.save()
        return Response(news_type_serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk=None):
        news_type = get_object_or_404(NewsType, id=pk)
        news_type.delete()
        return Response({"status": "news type has been deleted"}, status=status.HTTP_204_NO_CONTENT)


class NewsItemsViewset(ViewSet):
    permission_classes = [permissions.AllowAny]

    def list(self, request):
        news_type_name = self.request.query_params.get('news_type')
        news_items_qs = NewsItem.objects.all()
        if news_type_name:
            news_type_obj = get_object_or_404(NewsType, name=news_type_name)
            news_items_qs = news_items_qs.filter(news_type=news_type_obj)
        news_items_serializer = NewsItemSerializer(news_items_qs, many=True)
        return Response(news_items_serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, pk=None):
        news_item = get_object_or_404(NewsItem, id=pk)
        news_items_serializer = NewsItemSerializer(news_item)
        return Response(news_items_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        news_item_serializer = NewsItemSerializer(data=request.data)
        news_item_serializer.is_valid(raise_exception=True)
        news_item_serializer.save()
        return Response({"status": f"news item has been created"}, status=status.HTTP_201_CREATED)
    
    def update(self, request, pk=None):
        news_item = get_object_or_404(NewsItem, id=pk)
        news_item_serializer = NewsItemSerializer(instance=news_item, data=request.data)
        news_item_serializer.is_valid(raise_exception=True)
        news_item_serializer.save()
        return Response(news_item_serializer.data, status=status.HTTP_200_OK)
    
    def delete(self, request, pk=None):
        news_item = get_object_or_404(NewsItem, id=pk)
        news_item.delete()
        return Response({"status": "news item has been deleted"}, status=status.HTTP_204_NO_CONTENT)

