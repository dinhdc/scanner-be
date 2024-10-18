from django.urls import path, include

from app.api.urls import urlpatterns as api_urls
from app.fe.urls import urlpatterns as fe_urls

urlpatterns = [

]

urlpatterns += api_urls
