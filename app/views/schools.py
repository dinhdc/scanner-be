from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app import models
from app import serializers
from app import swaggers
from app.core import handle_paginate
from app.serializers.users import UserSerializer


class SchoolListAPIView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        user = self.request.user
        if user.is_superuser or user.is_staff:
            return models.School.objects.all()
        school_id_list = list(set(models.Staff.objects.filter(user=user).values_list('school_id', flat=True)))
        return models.School.objects.filter(id__in=school_id_list)

    @swagger_auto_schema(
        tags=["School"],
        manual_parameters=swaggers.school_list_params,
        operation_id="school_list",
        operation_summary="school list api",
        responses={
            200: swaggers.school_list_response
        }
    )
    def get(self, request, *args, **kwargs):
        school_list = self.get_queryset()
        res = handle_paginate(school_list, request, serializers.SchoolSerializer)
        res["code"] = 200
        res["message"] = "Success"
        res["msgCode"] = "success"
        return Response(
            res,
            status=200,
        )

    @swagger_auto_schema(
        tags=["School"],
        operation_id="school_create",
        operation_summary="school create api",
        request_body=swaggers.school_create_params,
        responses={
            200: swaggers.school_create_response,
            400: swaggers.base_error_response,
        }
    )
    def post(self, request, *args, **kwargs):
        name = request.data['name']
        code = request.data['code']
        try:
            school = models.School.objects.create(name=name, code=code)
            return Response(
                {
                    "code": 200,
                    "message": "Success",
                    "msgCode": "success",
                    "data": {
                        "id": school.id,
                        "name": name,
                        "code": code,
                    },
                },
                status=200,
            )
        except Exception as e:
            return Response(
                {
                    "code": 400,
                    "message": str(e),
                    "msgCode": "error",
                },
                status=400
            )


class StaffInSchoolAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["School"],
        operation_id="staff_in_school",
        operation_summary="Staff in school api",
        manual_parameters=swaggers.staff_in_school_request,
        responses={
            200: swaggers.staff_in_school_response
        }
    )
    def get(self, request, *args, **kwargs):
        school_id = request.GET.get('school')
        staffs = models.Staff.objects.filter(school_id=school_id).values_list("user_id", flat=True)
        users = User.objects.filter(id__in=staffs)
        res = handle_paginate(
            users,
            request,
            UserSerializer
        )
        res["code"] = 200
        res["message"] = "Success"
        res["msgCode"] = "success"
        return Response(
            res,
            status=200,
        )
