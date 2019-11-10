import urllib

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response

from api.evaler.LufthansaAPI import NearestAirport
from api.evaler.models import *
from .serializers import *
from django.conf import settings


class ParticipantViewSet(viewsets.ModelViewSet):
    queryset = Participant.objects.all()
    serializer_class = ParticipantSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        pk = kwargs['pk']
        near = NearestAirport().get_airport(Participant.objects.get(pk=pk).city)
        print(near)
        return Response(serializer.data)


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        pk = kwargs['pk']
        near = NearestAirport().get_airport(Event.objects.get(pk=pk).city)
        print(near)
        return Response(serializer.data)


@api_view(['GET'])
def travelplan(request, *args, **kwargs):
    print(kwargs)
    pid = kwargs['pid']
    eid = kwargs['eid']
    participant = Participant.objects.get(pk=pid)
    event = Event.objects.get(pk=eid)
    startport = NearestAirport().get_airport(participant.city)
    start_country = participant.country
    endport = NearestAirport().get_airport(event.city)
    end_country = event.country
    arrivaldate = event.start_time.date()
    departuredate = event.end_time.date()
    start_route = localtransport(participant.city, startport)
    end_route = localtransport(endport, event.city)
    return Response({'start':startport,'start-country':start_country,
                     'end':endport,'end-country':end_country,
                     'arrival':arrivaldate,'departure':departuredate,
                     'start-route':start_route,
                     'end-route':end_route})


def localtransport(start, end):
    start = urllib.parse.quote_plus(start)
    end = urllib.parse.quote_plus(end)
    api_string = f'https://maps.googleapis.com/maps/api/directions/json?origin={start}&destination={end}&key={settings.API_KEY_GOOGLE}'
    return api_string