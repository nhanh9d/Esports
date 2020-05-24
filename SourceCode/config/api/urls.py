#from django.conf.urls import url, include
from django.urls import include, path
from rest_framework import routers
from api.views import *

router = routers.DefaultRouter()
router.register('users', UserViewSet)
router.register('articles', ArticleViewSet)
router.register('status', StatusViewSet)
router.register('region', RegionViewSet)
router.register('games', GameViewSet)
router.register('leagues', LeagueViewSet)
router.register('teams', TeamViewSet)
router.register('matches', MatchViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls'))
]