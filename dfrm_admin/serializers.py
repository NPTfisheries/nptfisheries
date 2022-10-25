#dfrm_admin/serializers.py
from rest_framework import serializers

from locations.serializers import PointSerializer
from .models import Employee, Facility, Department, Division, Project, Subproject, Task
from locations.models import Location

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'

class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Department
        fields = '__all__'

class DivisionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Division
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'
        depth = 0

class SubprojectSerializer(serializers.ModelSerializer):
    #tasks = serializers.StringRelatedField(many=True)
    class Meta:
        model = Subproject
        fields = '__all__'
        #fields = ('id', 'name', 'tasks')
        depth = 0

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'
        #fields = ('id', 'name', 'location')
        # set depth to return parent tables
        depth = 0