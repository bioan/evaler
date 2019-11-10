from django.conf.urls import url
from django.urls import include, path
from rest_framework import routers

from api.evaler.views import travelplan
from . import views

router = routers.DefaultRouter()
router.register(r'participants', views.ParticipantViewSet)
router.register(r'events', views.EventViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    # path('api/participants/events/', travelplan),
    path('api/participants/<int:pid>/events/<int:eid>/', travelplan),
    url('api/', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]