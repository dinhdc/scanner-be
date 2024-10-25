from drf_yasg import openapi

school_instance_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="id of school", default=0),
        "code": openapi.Schema(type=openapi.TYPE_STRING, description="code of school", ),
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of school", ),
    }
)

event_instance_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="id of event", default=0),
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of event", ),
        "start_date": openapi.Schema(type=openapi.TYPE_STRING, description="start date",
                                     format="%Y-%m-%d %H:%M:%S"),
        "end_date": openapi.Schema(type=openapi.TYPE_STRING, description="end date",
                                   format="%Y-%m-%d %H:%M:%S"),
        "description": openapi.Schema(type=openapi.TYPE_STRING, description="description", ),
        "school": school_instance_schema
    }
)

user_instance_schema = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "id": openapi.Schema(type=openapi.TYPE_INTEGER, description="id of user", default=0),
        "username": openapi.Schema(type=openapi.TYPE_STRING, description="username", ),
        "email": openapi.Schema(type=openapi.TYPE_STRING, description="email", ),
        "first_name": openapi.Schema(type=openapi.TYPE_STRING, description="first name", ),
        "last_name": openapi.Schema(type=openapi.TYPE_STRING, description="last name", ),
    }
)
