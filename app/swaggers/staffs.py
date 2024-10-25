from drf_yasg import openapi

add_staff_to_school_req = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "user": openapi.Schema(type=openapi.TYPE_INTEGER, description="id of user"),
        'school': openapi.Schema(type=openapi.TYPE_INTEGER, description="id of school"),
    },
    required=["user", "school"],
)

add_staff_to_school_res = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code of status response", default=200),
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="success", default="Success"),
        "msgCode": openapi.Schema(type=openapi.TYPE_INTEGER, description="msgCode", default="success"),
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
            },
            default={}
        )

    }
)
