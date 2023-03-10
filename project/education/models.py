from django.db import models


class School(models.Model):
    name = models.CharField(max_length=64, unique=True)
    address = models.CharField(max_length=128)


class SchoolClass(models.Model):
    grade = models.IntegerField()
    school = models.ForeignKey(School, on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=64)
    school_class = models.ForeignKey(SchoolClass, on_delete=models.CASCADE)
