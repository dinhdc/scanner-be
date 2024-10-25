from drf_yasg import openapi
from .base import paginate_request

school_list_params = [

                     ] + paginate_request

school_list_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code of status response", default=200),
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="success", default="Success"),
        "msgCode": openapi.Schema(type=openapi.TYPE_INTEGER, description="msgCode", default="success"),
        "count": openapi.Schema(type=openapi.TYPE_INTEGER, description="total records filtered", default=0),
        "previous": openapi.Schema(type=openapi.TYPE_STRING, description="link of previous page if has"),
        "next": openapi.Schema(type=openapi.TYPE_STRING, description="link of next page if has"),
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="id of school", default=0),
                "code": openapi.Schema(type=openapi.TYPE_STRING, description="code of school", ),
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of school", ),
            }
        )

    }
)

school_create_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_STRING, description="code of school"),
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of school"),
    },
    required=["code", "name"],
)

school_create_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code of status response", default=200),
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="success", default="Success"),
        "msgCode": openapi.Schema(type=openapi.TYPE_INTEGER, description="msgCode", default="success"),
        "data": openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="id of school", default=0),
                "code": openapi.Schema(type=openapi.TYPE_STRING, description="code of school", ),
                "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of school", ),
            }
        )

    }
)
