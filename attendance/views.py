from django.shortcuts import render
from .models import Attendance, Group, Students
from .serializers import AttendanceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class AttendanceView(APIView):
    def post(self, request):
        data = request.data
        group_id = data["group_id"]
        attendance_day = data["attendance_day"]
        result = Attendance.objects.filter(students__group_id=group_id,  # studentga ulangan grpid = group_id
                                           created_at=attendance_day)
        serializers = AttendanceSerializer(result, many=True)
        return Response(serializers.data)
