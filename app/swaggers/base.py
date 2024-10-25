from drf_yasg import openapi

base_error_response = openapi.Schema(
    type=openapi.TYPE_OBJECT,
    properties={
        "code": openapi.Schema(type=openapi.TYPE_INTEGER, description="code of status response"),
        "message": openapi.Schema(type=openapi.TYPE_STRING, description="message of error"),
        "msgCode": openapi.Schema(type=openapi.TYPE_INTEGER, description="msgCode of error"),
    }
)

paginate_request = [
    openapi.Parameter("limit", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description="limit of paginate request"),
    openapi.Parameter("offset", openapi.IN_QUERY, type=openapi.TYPE_INTEGER, description="offset of paginate request"),
]
