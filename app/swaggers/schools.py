from drf_yasg import openapi
from .base import paginate_request
from app import serializers
from .schemas import school_instance_schema, user_instance_schema

school_list_params = [

                     ] + paginate_request

staff_in_school_request = [
                              openapi.Parameter("school", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                                                description="id of school", required=True),
                          ] + paginate_request

staff_in_school_response = openapi.Schema(
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
            items=user_instance_schema
        )

    }

)


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
            type=openapi.TYPE_ARRAY,
            items=school_instance_schema
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
        "data": school_instance_schema
    }
)
