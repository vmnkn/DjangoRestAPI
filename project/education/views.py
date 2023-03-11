from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import permissions

from .serializers import *
from .models import *


class SchoolViewset(viewsets.ModelViewSet):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolClassViewset(viewsets.ModelViewSet):
    queryset = SchoolClass.objects.all()
    serializer_class = SchoolClassSerializer


class StudentViewset(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        queryset = Student.objects.all()
        school_id = self.request.query_params.get('school_id', None)
        school_class_id = self.request.query_params.get('school_class_id', None)
        if school_id is not None:
            queryset = queryset.filter(school_class_id=school_id)
        if school_class_id is  not None:
            queryset = queryset.filter(school_class_id=school_class_id)
        return queryset
