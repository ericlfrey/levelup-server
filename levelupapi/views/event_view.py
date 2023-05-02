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
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data)

        # service_tickets = []
  #
  #
        # if request.auth.user.is_staff:
        # service_tickets = ServiceTicket.objects.all()
        #
        # if "status" in request.query_params:
        # if request.query_params['status'] == "done":
        # service_tickets = service_tickets.filter(date_completed__isnull=False)
        #
        # else:
        # service_tickets = ServiceTicket.objects.filter(customer__user=request.auth.user)
        #
        # serialized = ServiceTicketSerializer(service_tickets, many=True)
        # return Response(serializederialized.data, status=status.HTTP_200_OK)


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
