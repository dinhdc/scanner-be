from django.urls import path

from app.views import schools

schoolpatterns = [
    path("", schools.SchoolListAPIView.as_view(), name="schools"),
    path("staffs/", schools.StaffInSchoolAPIView.as_view(), name="staffs"),
]
