from drf_yasg.utils import swagger_auto_schema
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from app import swaggers
from app import serializers
from app import models
from app.core import handle_paginate


class EventsView(APIView):
    permission_classes = [IsAuthenticated]
    pagination_class = LimitOffsetPagination

    @swagger_auto_schema(
        tags=['Events'],
        operation_summary='Events',
        operation_description='Get all events',
        manual_parameters=swaggers.event_list_params,
        responses={
            200: swaggers.event_list_response
        }
    )
    def get(self, request):
        events = models.Event.objects.all()
        school = request.GET.get('school')
        if school:
            events = events.filter(school_id=school)
        res = handle_paginate(
            events,
            request,
            serializers.EventSerializer
        )
        res["code"] = 200
        res["message"] = "Success"
        res["msgCode"] = "success"
        return Response(
            res,
            status=200,
        )

    @swagger_auto_schema(
        tags=["Events"],
        operation_id="create_new_event",
        operation_summary="Create a new event",
        operation_description="Create a new event",
        request_body=swaggers.event_create_params,
        responses={
            201: swaggers.event_create_response,
        }
    )
    def post(self, request):
        serializer = serializers.EventCreateSerializer(data=request.data, context={"request": request})
        serializer.is_valid(raise_exception=True)
        event = serializer.save()
        event.created_by = request.user
        event.save()
        return Response(
            {
                "code": 201,
                "message": "Event created",
                "msgCode": "success",
                "data": serializers.EventSerializer(event).data,
            },
            status=201
        )
