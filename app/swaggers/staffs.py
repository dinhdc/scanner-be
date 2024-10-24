from drf_yasg import openapi
from .base import paginate_request
from .schemas import user_instance_schema

staff_list_req = [

] + paginate_request

staff_list_res = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code of status response", default=200),
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="success", default="Success"),
        "msgCode": openapi.Schema(type=openapi.TYPE_INTEGER, description="msgCode", default="success"),
        "count": openapi.Schema(type=openapi.TYPE_INTEGER, description="total records filtered", default=0),
        "previous": openapi.Schema(type=openapi.TYPE_STRING, description="link of previous page if has"),
        "next": openapi.Schema(type=openapi.TYPE_STRING, description="link of next page if has"),
        "data": openapi.Schema(
            type=openapi.TYPE_ARRAY,
            items=user_instance_schema,
        )

    }
)

add_staff_to_school_req = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "users": openapi.Schema(type=openapi.TYPE_ARRAY, items=openapi.Schema(
            type=openapi.TYPE_INTEGER
        ), description="list id of user"),
        'school': openapi.Schema(type=openapi.TYPE_INTEGER, description="id of school"),
    },
    required=["users", "school"],
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
