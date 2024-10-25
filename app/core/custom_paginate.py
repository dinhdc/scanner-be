from typing import Type

from rest_framework.pagination import LimitOffsetPagination
from rest_framework.serializers import ModelSerializer
from django.http import HttpRequest
from django.db.models.query import QuerySet


def handle_paginate(queryset: QuerySet, request: HttpRequest, serializer_class: Type[ModelSerializer]) -> dict:
    paginator = LimitOffsetPagination()

    # Paginate the queryset based on the request
    paginated_queryset = paginator.paginate_queryset(queryset, request)

    # Serialize the paginated queryset
    data = serializer_class(paginated_queryset, many=True).data

    count = paginator.count
    next_page = paginator.get_next_link()
    previous_page = paginator.get_previous_link()
    return {
        'count': count,
        'next': next_page,
        'previous': previous_page,
        'data': data
    }
