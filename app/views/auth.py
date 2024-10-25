from drf_yasg.utils import swagger_auto_schema
from rest_framework.authtoken.models import Token
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User

from app import swaggers as swg


class AuthLoginView(APIView):
    permission_classes = [AllowAny]

    @swagger_auto_schema(
        tags=['Auth'],
        responses={
            200: swg.login_success_response,
            400: swg.base_error_response,
            404: swg.base_error_response,
        },
        request_body=swg.login_request,
    )
    def post(self, request):
        # get username and password to check
        username = request.data['username']
        password = request.data['password']
        try:
            user = User.objects.get(username=username)
            if not user.check_password(password):
                return Response(
                    {
                        "code": 400,
                        "message": "Password is incorrect",
                        "msgCode": "password_wrong"
                    },
                    status=400
                )
            token, created = Token.objects.get_or_create(user=user)
            return Response(
                {
                    "code": 200,
                    "message": "Successfully logged in",
                    "msgCode": "success",
                    "data": {
                        "token": token.key,
                        "profile": {
                            "username": username,
                            "email": user.email,
                            "first_name": user.first_name,
                            "last_name": user.last_name,
                            "is_staff": user.is_staff,
                        }
                    }
                },
                status=200
            )
        except User.DoesNotExist:
            return Response(
                {
                    "code": 404,
                    "message": "User does not exist",
                    "msgCode": "user_not_found"
                },
                status=404
            )
