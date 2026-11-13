from rest_framework import viewsets, filters
from rest_framework.permissions import (DjangoModelPermissionsOrAnonReadOnly)
from django_filters.rest_framework import DjangoFilterBackend
from .models import Course
from .serializers import CourseSerializer

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]
filter_backends = [
    DjangoFilterBackend, filters.SearchFilter
]
filterset_fields = ["formateur"]
search_fields = ["title", "description"]
