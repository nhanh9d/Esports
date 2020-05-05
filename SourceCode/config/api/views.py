from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

from api.models import User
from api.serializers import UserSerializer

#permissions
from rest_framework.permissions import AllowAny
from api.permissions import IsLoggedInUserOrAdmin, IsAdminUser

#Paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#Response
from rest_framework.response import Response

from rest_framework.decorators import api_view, renderer_classes
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
        print(self)
        return [permission() for permission in permission_classes]

def user_list(request):
    data = []
    nextPage = 1
    previousPage = 1
    users = User.objects.all()
    page = request.GET.get('page', 1)
    limit = request.GET.get('limit', 20)
    paginator = Paginator(users, limit)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    
    serializer = UserSerializer(data,context={'request': request} ,many=True)
    
    return Response({'data': serializer.data , 'count': paginator.count})