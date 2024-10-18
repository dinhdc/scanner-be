import datetime

from django.contrib.auth.models import User
from drf_yasg.utils import swagger_auto_schema
from rest_framework.permissions import IsAuthenticated

from app.models import Ticket
from app.serializers import user as user_serializer
from app.serializers import tickets as ticket_serializer
from rest_framework import viewsets
from rest_framework.response import Response


class UserViewSet(viewsets.ViewSet):
    """
    API endpoint for create new users
    """

    @swagger_auto_schema(
        tags=['AUTH'],
        request_body=user_serializer.UserCreateSerializer,
    )
    def create(self, request):
        data = request.data
        serializer = user_serializer.UserSerializer(data=data)
        if serializer.is_valid():
            password = data.get('password')
            user = serializer.save()
            user.set_password(password)
            user.save()
            res_serializer = user_serializer.UserSerializer(user)
            return Response(res_serializer.data, status=200)
        return Response(serializer.errors, status=400)


class UserLoginViewSet(viewsets.ViewSet):

    @swagger_auto_schema(
        tags=['AUTH'],
        request_body=user_serializer.UserLoginReqSerializer,
        responses={200: user_serializer.UserLoginResSerializer},
    )
    def create(self, request):
        username = request.data["username"]
        password = request.data["password"]
        user = User.objects.filter(username=username).first()
        if not user:
            return Response({'error': 'User not found'}, status=404)
        if not user.check_password(password):
            return Response({'error': 'Invalid credentials'}, status=403)
        serializer = user_serializer.UserLoginResSerializer(user)
        return Response(serializer.data, status=200)


class TicketViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['TICKETS'],
        manual_parameters=[]
    )
    def list(self, request):
        """
        List all tickets for a user.
        """
        tickets = Ticket.objects.all()
        is_admin = request.user.is_staff or request.user.is_superuser
        if not is_admin:
            tickets = tickets.filter(user=request.user)
        print(tickets.count())
        tickets = tickets.order_by('-id')
        serializers = ticket_serializer.TicketResSerializer(tickets, many=True)
        return Response(serializers.data, status=200)

    @swagger_auto_schema(
        tags=['TICKETS'],
        request_body=ticket_serializer.TicketCreateSerializer,
        responses={201: ticket_serializer.TicketResSerializer},
    )
    def create(self, request):
        """
        Create a new ticket for a user.
        """
        serializer = ticket_serializer.TicketCreateSerializer(data=request.data)
        if serializer.is_valid():
            ticket = serializer.save()
            serializer = ticket_serializer.TicketResSerializer(ticket)
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class TicketCheckInViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
        tags=['TICKETS'],
        request_body=ticket_serializer.TicketCheckInSerializer,
        responses={200: ticket_serializer.TicketResSerializer},
    )
    def create(self, request):
        user = request.user
        code = request.data['code']
        ticket = Ticket.objects.filter(code=code, user=user).first()
        if not ticket:
            return Response({
                "code": 404,
                "message": "Ticket not found"
            }, status=200)
        ticket.checkin_at = datetime.datetime.now()
        ticket.save()
        serializer = ticket_serializer.TicketResSerializer(ticket)
        return Response(serializer.data, status=200)
