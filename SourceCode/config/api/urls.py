#from django.conf.urls import url, include
from django.urls import include, path
from rest_framework import routers
from api.views import UserViewSet, ArticleViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('articles', ArticleViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls'))
]