from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from .serializers import PrivilegeSerializer, RoleSerializer, PersonSerializer, DataSerializer, ExampleSerializer

from app.models import Privilege, Role, Person, Data, Example


class PrivilegeApi(ListCreateAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer


class PrivilegeDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Privilege.objects.all()
    serializer_class = PrivilegeSerializer


class RoleApi(ListCreateAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class RoleDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializer


class PersonApi(ListCreateAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class PersonDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Person.objects.all()
    serializer_class = PersonSerializer


class DataApi(ListCreateAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class DataDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class ExampleApi(ListCreateAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer


class ExampleDetailApi(RetrieveUpdateDestroyAPIView):
    queryset = Example.objects.all()
    serializer_class = ExampleSerializer
