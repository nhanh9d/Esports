from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import *
from api.serializers import *

#permissions
from rest_framework.permissions import AllowAny
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser

#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Response
from rest_framework.response import Response

from rest_framework.decorators import api_view, renderer_classes, action
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    

class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
    

class StatusViewSet(viewsets.ModelViewSet):
    queryset = Status.objects.filter(is_delete=False)
    serializer_class = StatusSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['GET'])
    def get_active_status(self, request, pk=None):
        status = Status.objects.filter(is_active=True).filter(is_delete=False).values('status_id', 'name')
        serializer = self.get_serializer(status, many=True)
        return Response(serializer.data)
    

class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['GET'])
    def get_active_regions(self, request, pk=None):
        regions = Region.objects.filter(is_active=True).filter(is_delete=False).values('region_id', 'name')
        serializer = self.get_serializer(regions, many=True)
        return Response(serializer.data)
    

class GameViewSet(viewsets.ModelViewSet):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['GET'])
    def get_active_games(self, request, pk=None):
        games = Game.objects.filter(is_active=True).filter(is_delete=False)
        serializer = self.get_serializer(games, many=True)
        return Response(serializer.data)

class LeagueViewSet(viewsets.ModelViewSet):
    queryset = League.objects.all()
    serializer_class = LeagueSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['GET'])
    def get_active_leagues(self, request, pk=None):
        leagues = League.objects.filter(is_active=True).filter(is_delete=False)
        serializer = self.get_serializer(leagues, many=True)
        return Response(serializer.data)

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]

    @action(detail=False, methods=['GET'])
    def get_active_teams(self, request, pk=None):
        teams = Team.objects.filter(is_active=True).filter(is_delete=False)
        serializer = self.get_serializer(teams, many=True)
        return Response(serializer.data)

class MatchViewSet(viewsets.ModelViewSet):
    queryset = Match.objects.all()
    serializer_class = MatchSerializer

    # Add this code block
    def get_permissions(self):
        permission_classes = []
        if self.action == 'create':
            permission_classes = [AllowAny]
        elif self.action == 'retrieve' or self.action == 'update' or self.action == 'partial_update':
            permission_classes = [AllowAny]
        elif self.action == 'list' or self.action == 'destroy':
            permission_classes = [AllowAny]
        return [permission() for permission in permission_classes]
