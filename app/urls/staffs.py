from django.urls import path

from app.views import staff

staff_urls = [
    path('add-to-school/', staff.AddStaffToSchoolAPIView.as_view(), name='add-staff-to-school'),
    path("list/", staff.ListUserAPIView.as_view(), name='list-staff'),
]
