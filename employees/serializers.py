from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Employee
        # fields = "__all__"
        fields = ["id", "name", "role", "salary","department", "email"]

    def validate_salary(self, value):

        if value < 0:
            raise serializers.ValidationError(
                "salary cannot be negative"
            )
        return value