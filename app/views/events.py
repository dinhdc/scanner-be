from django.utils import timezone
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
        school = models.Staff.objects.filter(user=request.user).first().school
        events = models.Event.objects.filter(school=school)
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
        data = request.data
        data["school_id"] = models.Staff.objects.filter(user=request.user).first().school
        serializer = serializers.EventCreateSerializer(data=data, context={"request": request})
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


class EventParticipantAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Events"],
        operation_id="event_participant_list",
        operation_summary="List event participants",
        operation_description="List event participants",
        manual_parameters=swaggers.event_participant_list_params,
        responses={
            200: swaggers.event_participant_list_response
        }
    )
    def get(self, request):
        event = request.GET.get('event')
        participants = models.EventParticipator.objects.filter(event_id=int(event))
        res = handle_paginate(
            participants,
            request,
            serializers.EventParticipantSerializer
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
        operation_id="create_new_event_participant",
        operation_summary="Create a new event participant",
        request_body=swaggers.event_participant_create_req,
        responses={
            200: swaggers.event_participant_create_res
        }
    )
    def post(self, request):
        name = request.data["name"]
        event = request.data["event"]
        participant = models.EventParticipator.objects.create(
            event_id=event,
            name=name,
            created_by=request.user
        )
        participant.generate_code()
        return Response(
            {
                "code": 200,
                "message": "Success",
                "msgCode": "success",
                "data": serializers.EventParticipantSerializer(participant).data,
            },
            status=200
        )


class EventParticipantDetailAPIView(APIView):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=["Events"],
        operation_id="event_participant_detail",
        operation_summary="Get event participant detail",
        operation_description="Get event participant detail",
        responses={
            200: swaggers.event_participant_create_res,
            404: swaggers.base_error_response,
        }
    )
    def get(self, request, code):
        try:
            participant = models.EventParticipator.objects.get(code=code)
            serializer = serializers.EventParticipantSerializer(participant)
            return Response(
                {
                    "code": 200,
                    "message": "Success",
                    "msgCode": "success",
                    "data": serializer.data,
                },
                status=200
            )
        except models.EventParticipator.DoesNotExist:
            return Response(
                {
                    "code": 404,
                    "message": "Participant not found",
                    "msgCode": "participant_not_found"
                },
                status=404
            )

    @swagger_auto_schema(
        tags=["Events"],
        operation_id="update_event_participant",
        operation_summary="Update event participant checked in",
        responses={
            200: swaggers.event_participant_create_res,
            404: swaggers.base_error_response,
        }
    )
    def patch(self, request, code):
        try:
            participant = models.EventParticipator.objects.get(code=code)
            participant.checkin_at = timezone.now()
            participant.checkin_by = request.user
            participant.save()
            # TODO: send real time guest checkin at event
            serializer = serializers.EventParticipantSerializer(participant)
            return Response(
                {
                    "code": 200,
                    "message": "Participant checked in",
                    "msgCode": "success",
                    "data": serializer.data,
                },
                status=200
            )
        except models.EventParticipator.DoesNotExist:
            return Response(
                {
                    "code": 404,
                    "message": "Participant not found",
                    "msgCode": "participant_not_found"
                },
                status=404
            )
