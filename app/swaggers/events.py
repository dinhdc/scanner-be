from drf_yasg import openapi
from .base import paginate_request
from .schemas import event_instance_schema, participant_event_schema

event_list_params = [
                    ] + paginate_request

event_list_response = openapi.Schema(
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
            items=event_instance_schema
        )

    }
)

event_create_params = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of event"),
        "start_date": openapi.Schema(type=openapi.TYPE_STRING, description="start date", format="%Y-%m-%d %H:%M:%S"),
        "end_date": openapi.Schema(type=openapi.TYPE_STRING, description="end date", format="%Y-%m-%d %H:%M:%S"),
        "description": openapi.Schema(type=openapi.TYPE_STRING, description="description", format="text/plain"),
    },
    required=["code", "name"],
)

event_create_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code of status response", default=200),
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="success", default="Success"),
        "msgCode": openapi.Schema(type=openapi.TYPE_INTEGER, description="msgCode", default="success"),
        "data": event_instance_schema

    }
)

event_participant_list_params = [
                                    openapi.Parameter("event", in_=openapi.IN_QUERY, type=openapi.TYPE_INTEGER,
                                                      description="id of event", required=True)
                                ] + paginate_request

event_participant_list_response = openapi.Schema(
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
            items=participant_event_schema
        )

    }
)
event_participant_create_req = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "event": openapi.Schema(type=openapi.TYPE_INTEGER, description="id of event"),
        "name": openapi.Schema(type=openapi.TYPE_STRING, description="name of participant")
    },
    required=["event", "name"]
)

event_participant_create_res = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code of status response", default=200),
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="success", default="Success"),
        "msgCode": openapi.Schema(type=openapi.TYPE_INTEGER, description="msgCode", default="success"),
        "data": participant_event_schema,
    }
)
