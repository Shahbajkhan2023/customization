from django.urls import path
# from .views import BookListCreateAPIView


# urlpatterns = [
#     path('books/', BookListCreateAPIView.as_view(), name='book-list-create'),
# ]


from rest_framework.routers import DefaultRouter
from .views import BookViewSet

router = DefaultRouter()
router.register(r'books', BookViewSet, basename='book')


urlpatterns = router.urls

