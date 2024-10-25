from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Staff
from app import swaggers

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
        user_id = request.data["user"]
        school_id = request.data["school"]
        # check if exist
        exits = Staff.objects.filter(user__id=user_id, school__id=school_id).exists()
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
