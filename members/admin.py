from django.contrib import admin
from .models import Member, Course, Registration, Ticket, Reply

admin.site.register(Member)
admin.site.register(Course)
admin.site.register(Registration)


admin.site.register(Ticket)
admin.site.register(Reply)