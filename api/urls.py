from rest_framework import routers
from .views import NewsTypesViewset, NewsItemsViewset

app_name='news_curd'

router = routers.SimpleRouter()
router.register(r'news-types', NewsTypesViewset, basename="news-types")
router.register(r'news-items', NewsItemsViewset, basename="news-items")
urlpatterns = router.urls
