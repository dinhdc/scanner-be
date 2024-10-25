from django.urls import include, path

from .auth import urlpatterns as auth_url, urlpatterns
from .schools import schoolpatterns
from .staffs import staff_urls

urlpatterns = [
    path('auth/', include(auth_url)),
    path('schools/', include(schoolpatterns)),
    path('staffs/', include(staff_urls))
]
