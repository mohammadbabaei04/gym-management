from rest_framework import serializers
from .models import Course, Member, Registration, Ticket



class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'description',
                   'price', 'capacity', 'start_data', 'end_data']
        

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ['id', 'user', 'phone', 'address', 'joined_at']


class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registration
        fields = ['id', 'member', 'course', 'registered_at']


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ['id', 'user', 'subject', 'message',
                   'created_at', 'is_resolved']
