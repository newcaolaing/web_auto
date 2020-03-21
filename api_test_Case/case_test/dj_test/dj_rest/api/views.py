import sys
sys.path.append("D:\mypythonpro\web_auto\api_test_Case\case_test\dj_test\dj_rest")

from django.shortcuts import render
from django.contrib.auth.models import User,Group
from rest_framework import viewsets
from api.serializers import Userserializer,Groupserializer

# Create your views here.
class Userviewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = Userserializer

class Groupviewset(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = Groupserializer