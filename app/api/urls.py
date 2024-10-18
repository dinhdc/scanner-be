from app.api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'api/register', views.UserViewSet, basename='register')
router.register(r'api/login', views.UserLoginViewSet, basename='login')
router.register(r'api/tickets', views.TicketViewSet, basename='tickets')
router.register(r'api/ticket-checkin', views.TicketCheckInViewSet, basename='ticket-checkin')
urlpatterns = router.urls
