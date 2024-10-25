from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app import models
from app import serializers
from app import swaggers


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
        paginator = self.pagination_class()
        paginated_schools = paginator.paginate_queryset(school_list, request)
        count = paginator.count
        next_page = paginator.get_next_link()
        previous_page = paginator.get_previous_link()
        page_query = paginator.paginate_queryset(paginated_schools, request)
        serializer = serializers.SchoolSerializer(page_query, many=True)
        return Response(
            {
                "code": 200,
                "message": "Success",
                "msgCode": "success",
                "count": count,
                "next": next_page,
                "previous": previous_page,
                "data": serializer.data,
            },
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
        manual_parameters=swaggers.paginate_request,
    )
    def get(self, request, school_id, *args, **kwargs):
        staffs = models.Staff.objects.filter(school_id=school_id)
