from django.urls import include, path

from .auth import urlpatterns as auth_url, urlpatterns
from .events import event_urls
from .schools import schoolpatterns
from .staffs import staff_urls

urlpatterns = [
    path('auth/', include(auth_url)),
    path('schools/', include(schoolpatterns)),
    path('staffs/', include(staff_urls)),
    path('schools/events/', include(event_urls))
]
