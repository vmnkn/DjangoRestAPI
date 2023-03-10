from .models import *
from rest_framework import serializers


class SchoolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = School
        fields = ['id', 'name', ]


class SchoolClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = SchoolClass
        fields = ['id', 'grade', ]


class StudentSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', ]