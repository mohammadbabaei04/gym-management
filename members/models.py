from django.db import models
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels


class Member(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    address = models.TextField(blank=True, null=True)
    joined_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
    


class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    capacity = models.IntegerField()
    start_data = jmodels.jDateTimeField()
    end_data = jmodels.jDateTimeField()

    def __str__(self):
        return self.name
    


class Registration(models.Model):
    member = models.ForeignKey(Member, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    registered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.member.user.username} - {self.course.name}"
    




class Ticket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_resolved = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - {self.subject}"



class Reply(models.Model):
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE, related_name='replies')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"پاسخ به {self.ticket.subject}"