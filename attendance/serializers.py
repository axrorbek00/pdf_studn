from rest_framework import serializers
from .models import Students, Group, Attendance


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = "__all__"


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = "__all__"


class AttendanceSerializer(serializers.ModelSerializer):
    fullname = serializers.SerializerMethodField()
    group = serializers.SerializerMethodField()

    def get_group(self, obj):
        return obj.students.group.name

    def get_fullname(self, obj):
        return obj.students.full_name

    class Meta:
        model = Attendance
        fields = "__all__"
