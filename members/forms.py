from django import forms
from .models import Member, Course, Ticket, Reply



class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['phone', 'address']


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['name', 'description', 'price', 'capacity', 'start_data', 'end_data']





class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['subject', 'message']


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['message']