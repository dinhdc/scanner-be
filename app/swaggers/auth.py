from drf_yasg import openapi

login_request = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "username": openapi.Schema(type=openapi.TYPE_STRING, ),
        "password": openapi.Schema(type=openapi.TYPE_STRING, ),
    },
    required=['username', 'password'],
)

login_success_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, ),
        "message": openapi.Schema(type=openapi.TYPE_STRING, ),
        "msgCode": openapi.Schema(type=openapi.TYPE_STRING, ),
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "token": openapi.Schema(type=openapi.TYPE_STRING, ),
                "profile": openapi.Schema(
                    type=openapi.TYPE_OBJECT,
                    properties={
                        "username": openapi.Schema(type=openapi.TYPE_STRING, ),
                        "email": openapi.Schema(type=openapi.TYPE_STRING, ),
                        "first_name": openapi.Schema(type=openapi.TYPE_STRING, ),
                        "last_name": openapi.Schema(type=openapi.TYPE_STRING, ),
                        "is_staff": openapi.Schema(type=openapi.TYPE_BOOLEAN, ),
                    }
                )
            }
        )
    }
)

