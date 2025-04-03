from rest_framework.test import APITestCase
from api.models import NewsType, NewsItem


class BaseTest(APITestCase):
    def setUp(self):
        self.news_type_1 = NewsType.objects.create(name="Sports", color="RED")
        self.news_item_1 = NewsItem.objects.create(title="Test sports title",
                                                   about="Test sports about info",
                                                   description="Test sports description textarea",
                                                   news_type=self.news_type_1)
        self.news_type_2 = NewsType.objects.create(name="Politics", color="BLACK")
        self.news_item_2 = NewsItem.objects.create(title="Test politics title",
                                                   about="Test politics about info",
                                                   description="Test politics description textarea",
                                                   news_type=self.news_type_2)
        self.news_type_3 = NewsType.objects.create(name="Video Games", color="WHITE")
        self.news_item_3 = NewsItem.objects.create(title="Test video games title",
                                                   about="Test video games about info",
                                                   description="Test video games description textarea",
                                                   news_type=self.news_type_3)

class APITestClass(BaseTest):
    def test_get_news_items(self):
        url = "http://127.0.0.1:8000/api/news-items/"
        response = self.client.get(url)
        news_items = response.json()
        first_news_item = news_items[0]
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(first_news_item)
        self.assertEqual(len(news_items), 3)
    
    
    def test_get_news_items_sports_type(self):
        url = "http://127.0.0.1:8000/api/news-items/?news_type=Sports"
        response = self.client.get(url)
        first_news_item = response.json()[0]
        self.assertEqual(response.status_code, 200)
        self.assertEqual(first_news_item["news_type_name"], "Sports")
        

    def test_get_news_item_by_id(self):
        url = "http://127.0.0.1:8000/api/news-items/1/"
        response = self.client.get(url)
        news_items = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(news_items)


    def test_post_news_item(self):
        post_json = {
            "title": "Sports article title",
            "about": "Short description of the sports article",
            "description": "Full description of the sports article",
            "news_type_name": "Sports",
            "news_type_color": "RED"
        }
        url = "http://127.0.0.1:8000/api/news-items/"
        response = self.client.post(url, post_json, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["status"], "news item has been created")


    def test_delete_news_item(self):
        news_item = NewsItem.objects.get(title="Test video games title")
        news_item_id = news_item.id
        news_item.delete()
        url = f"http://127.0.0.1:8000/api/news-items/{news_item_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        
    
    def test_get_news_types(self):
        url = "http://127.0.0.1:8000/api/news-types/"
        response = self.client.get(url)
        news_items = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(news_items), 3)
    

    def test_get_news_type_by_id(self):
        url = "http://127.0.0.1:8000/api/news-types/1/"
        response = self.client.get(url)
        news_items = response.json()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(news_items)


    def test_post_news_type(self):
        post_json = {
            "name": "IT",
            "color": "GREEN"
        }
        url = "http://127.0.0.1:8000/api/news-types/"
        response = self.client.post(url, post_json, format='json')
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["status"], "news type has been created")


    def test_delete_news_type(self):
        news_type = NewsType.objects.get(name="Video Games")
        news_type_id = news_type.id
        news_type.delete()
        url = f"http://127.0.0.1:8000/api/news-types/{news_type_id}/"
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
