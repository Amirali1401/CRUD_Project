
from django.urls import path

from rest_framework import routers

from . import views

router = routers.DefaultRouter()


router.register('book' , views.BookViewSet , basename = 'book')
router.register('category' , views.CategoryViewSet , basename = 'category')

urlpatterns = [
     path('<int:pk>/detail_book/' , views.DetailBookViewSet.as_view() , name = 'detail_book'),
     path('<int:pk>/detail_category/' , views.DetailCategoryViewSet.as_view() , name = 'detail_category')
]+router.urls



