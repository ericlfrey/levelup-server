"""View module for handling requests about event types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from levelupapi.models import Event


class EventView(ViewSet):
    """Level up event types view"""

    def retrieve(self, request, pk):
        """Handle GET requests for single event type
        Returns:
            Response -- JSON serialized event type
        """
        event = Event.objects.get(pk=pk)
        serializer = EventSerializer(event)
        return Response(serializer.data)

    def list(self, request):
        """Handle GET requests to get all event types
        Returns:
            Response -- JSON serialized list of event types
        """

        events = Event.objects.all()
        if "organizer" in request.query_params:
            events = events.filter(
                organizer_id=request.query_params['organizer'])
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)


class EventSerializer(serializers.ModelSerializer):
    """JSON serializer for event types
    """
    class Meta:
        model = Event
        fields = (
            'id',
            'organizer',
            'description',
            'date',
            'time',
            'attendees'
        )
        depth = 1
