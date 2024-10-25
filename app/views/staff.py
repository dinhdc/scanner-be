from django.contrib.auth.models import User
from django.db.models import Q
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.core import handle_paginate
from app.models import Staff
from app import swaggers
from app import serializers


class ListUserAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Staff"],
        operation_id="list_users",
        operation_summary="List users",
        manual_parameters=swaggers.staff_list_req,
        responses={
            200: swaggers.staff_list_res
        }
    )
    def get(self, request):
        users = User.objects.exclude(Q(is_staff=True) | Q(is_superuser=True))
        res = handle_paginate(
            users,
            request,
            serializers.UserSerializer,
        )
        res["code"] = 200
        res["message"] = "success"
        res["msgCode"] = "success"
        return Response(res, status=200)


class AddStaffToSchoolAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Staff"],
        operation_id="add_staff_to_school",
        operation_summary="Add Staff to School",
        request_body=swaggers.add_staff_to_school_req,
        responses={
            200: swaggers.add_staff_to_school_res
        }
    )
    def post(self, request, *args, **kwargs):
        list_user_id = request.data["users"]
        school_id = request.data["school"]
        staffs = Staff.objects.filter(school__id=school_id)
        for user_id in list_user_id:
            # check if exist
            exits = staffs.filter(user_id=user_id).exists()
            if not exits:
                Staff.objects.create(user_id=user_id, school_id=school_id)
        return Response(
            {
                "code": 200,
                "message": "Success",
                "msgCode": "success",
                "data": None
            },
            status=200
        )
