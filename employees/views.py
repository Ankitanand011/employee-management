# from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def hello(request):
    return HttpResponse("Hello Django")

def send(request):
    print(request.method)
    return HttpResponse("send money")

def get_employee(request, id):
    return HttpResponse(f"Employee ID is {id}")


#create Rest framework views
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .models import Employee, Department
from rest_framework.views import APIView
from .serializers import EmployeeSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import isAdmin
from django.shortcuts import get_object_or_404
from django.core.cache import cache

@api_view(["GET"])
def hello_api(request):
    return Response({
        "message": "Hello from Django rest framework"
    })

#get all employees
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def employee_list(request):

    cached_employees = cache.get("employees")

    if cached_employees is not None:
        return Response(cached_employees)

    employees = Employee.objects.all()

    serializer = EmployeeSerializer(
        employees,
        many=True
    )

    data = serializer.data

    cache.set(
        "employees",
        data,
        timeout=300
    )

    return Response(data)

    # data = []

    # for employee in employees:
    #     data.append({
    #         "id": employee.id,
    #         "name":employee.name,
    #         "role":employee.role,
    #         "salary":employee.salary,
    #         "email":employee.email,
    #     })

    # return Response(data)


class HelloApiView(APIView):

    def get(self, request):
        return Response({
            "message": "Hello from APIView"
        })

#create employee
@api_view(["POST"])
# @permission_classes([IsAuthenticated])
@permission_classes([isAdmin])
def create_employee(request):

    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#get employee by id
@api_view(["GET"])
@permission_classes([IsAuthenticated])
def employee_detail(request, id):

    # try:
    #     employee = Employee.objects.get(id=id)
    # except Employee.DoesNotExist:
    #     return Response(
    #         {"error": "Employee not found"},
    #         status=404
    #         )

    employee = get_object_or_404(
        Employee,
        id=id
    )

    serializer = EmployeeSerializer(employee)

    return Response(
        serializer.data,
        status=status.HTTP_200_OK
    )


#update employee records 
@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_employee(request, id):

    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(
            {"error": "Employee not found"},
            status=404
        )

    serializer = EmployeeSerializer(
        employee,
        data = request.data
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(
        serializer.errors,
        status=400
    )

#update employee partially
@api_view(["PATCH"])
@permission_classes([IsAuthenticated])
def partial_update_employee(request, id):

    try:
        employee = Employee.objects.get(id=id)
    except Employee.DoesNotExist:
        return Response(
            {"error": "Employee not found"},
            status=404
        )

    serializer = EmployeeSerializer(
        employee,
        data = request.data,
        partial = True
    )

    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data)

    return Response(serializer.errors, status=400)

# #delete employee -> only admin staff can delete this employee
# @api_view(["DELETE"])
# # @permission_classes([IsAuthenticated])
# @permission_classes([isAdmin])
# def delete_employee(request, id):

#     try:
#         employee = Employee.objects.get(id=id)
#     except Employee.DoesNotExist:
#         return Response(
#             {"error": "Employee not found"},
#             status=404
#         )

#     employee.delete()

#     return Response(
#         {"message": "Employee deleted successfully"},
#         status=204
#     )