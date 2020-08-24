from rest_framework import routers
from .views import ArticleSviewSet


router = routers.DefaultRouter() 

router.register(r"article", ArticleSviewSet, basename='article')