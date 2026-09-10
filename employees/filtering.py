from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeListView(ListAPIView):

    queryset = Employee.objects.all()

    serializer_class = EmployeeSerializer

    filter_backends = [
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter
    ]

    filterset_fields = [
        "role",
        "department"
    ]

    search_fields = [
        "name",
        "role"
    ]

    ordering_fields = [
        "name",
        "salary"
    ]

    ordering = [
            "-salary"
        ]