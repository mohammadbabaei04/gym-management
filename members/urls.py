from django.urls import path
from .views import CourseDetailView, CourseListView, MemberDetailView, MemberListView
from .views import register_for_course, edit_profile, admin_required, add_course
from .views import edit_course, delete_course, ticket_list, ticket_create, ticket_detail,admin_ticket_list
from .views import CourseDetailAPI, CourseListAPI

app_name = 'members'

urlpatterns = [
    path('courses/', CourseListView.as_view(), name='course_list'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course_detail'),
    path('members/', MemberListView.as_view(), name='member_list'),
    path('members/<int:pk>/', MemberDetailView.as_view(), name='member_detail'),
    path('register/<int:course_id>/', register_for_course, name='register_for_course'),
    path('profile/edit/', edit_profile, name='edit_profile'),
    path('add/', add_course, name='add_course'),
    path('courses/<int:pk>/edit/', edit_course, name='edit_course'),
    path('courses/<int:pk>/delete/', delete_course, name='delete_course'),
    path('tickets/', ticket_list, name='ticket_list'),
    path('tickets/new/', ticket_create, name='ticket_create'),
    path('tickets/<int:pk>/', ticket_detail, name='ticket_detail'),
    path('manage/tickets/', admin_ticket_list, name='admin_ticket_list'),
    path('api/courses/', CourseListAPI.as_view(), name='api_course_list'),
    path('api/courses/<int:pk>/', CourseDetailAPI.as_view(), name='api_course_detail'),
    ]