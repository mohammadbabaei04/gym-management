from django.shortcuts import redirect, get_object_or_404, render
from .models import Member, Course, Registration, Reply, Ticket
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .forms import MemberForm, CourseForm, ReplyForm, TicketForm
from .decorators import admin_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CourseSerializer
from django.db.models import Sum


# ---------------------لیست دوره ها-----------------------------------------
class CourseListView(ListView):
    model = Course
    template_name = 'members/course_list.html'
    context_object_name = 'courses'
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset()
        search_query = self.request.GET.get('q')
        if search_query:
            queryset = queryset.filter(name__icontains = search_query)

        return queryset



class CourseDetailView(DetailView):
    model = Course
    template_name = 'members/course_detail.html'
    context_object_name = 'course'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        course = self.get_object()
        already_registered = False

        if self.request.user.is_authenticated:
            member = self.request.user.member
            already_registered = Registration.objects.filter(member=member, course=course).exists()

        context['already_registered'] = already_registered
        return context


# ----------------------لیست اعضای باشگاه-----------------------------
class MemberListView(ListView):
    model = Member
    template_name = 'members/member_list.html'
    context_object_name = 'members'

class MemberDetailView(DetailView):
    model = Member
    template_name = 'members/member_detail.html'
    context_object_name = 'member'


# -----------------------ثبتنام----------------------------------------
@login_required
def register_for_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    member = request.user.member

    if Registration.objects.filter(member=member, course=course).exists():
        return redirect('members:course_detail', pk=course_id)

    Registration.objects.create(member=member, course=course)
    return redirect('members:course_detail', pk=course_id)



# -----------------------ویرایش پروفایل----------------------------------------
@login_required
def edit_profile(request):
    member = request.user.member
    if request.method == 'POST':
        form = MemberForm(request.POST, instance=member)
        if form.is_valid():
            form.save()
            return redirect('members:course_list')
    else:
        form = MemberForm(instance=member)
    return render(request, 'members/edit_profile.html', {'form': form})



# -----------------------افزودن دوره----------------------------------------
@admin_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('members:course_list')
    else:
        form = CourseForm()
    return render(request, 'members/add_course.html', {'form': form})



# -----------------------ویرایش دوره----------------------------------------
@admin_required
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('members:course_detail', pk=pk)
    else:
        form = CourseForm(instance=course)
    return render(request, 'members/edit_course.html', {'form': form, 'course': course})



# -----------------------حذف دوره----------------------------------------
@admin_required
def delete_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.delete()
        return redirect('members:course_list')
    return render(request, 'members/delete_course.html', {'course': course})




# -----------------------پشتیانی----------------------------------------
@login_required
def ticket_list(request):
    tickets = Ticket.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'members/ticket_list.html', {'tickets': tickets})



@login_required
def ticket_create(request):
    if request.method == 'POST':
        form = TicketForm(request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.user = request.user
            ticket.save()
            return redirect('members:ticket_list')
    else:
        form = TicketForm()
    return render(request, 'members/ticket_form.html', {'form': form})



@login_required
def ticket_detail(request, pk):
    ticket = get_object_or_404(Ticket, pk=pk)
    replies = ticket.replies.all().order_by('created_at')

    if request.method == 'POST' and request.user.is_staff:
        form = ReplyForm(request.POST)
        if form.is_valid():
            reply = form.save(commit=False)
            reply.ticket = ticket
            reply.user = request.user
            reply.save()
            return redirect('members:ticket_detail', pk=pk)
    else:
        form = ReplyForm()

    return render(request, 'members/ticket_detail.html', {
        'ticket': ticket,
        'replies': replies,
        'form': form,
    })



@admin_required
def admin_ticket_list(request):
    tickets = Ticket.objects.all().order_by('-created_at')
    return render(request, 'members/admin_ticket_list.html', {'tickets': tickets})



# -----------------------API----------------------------------------
class CourseListAPI(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)
        return Response(serializer.data)
    

class CourseDetailAPI(APIView):
    def get(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        serializer = CourseSerializer(course)
        return Response(serializer.data)
    



# -----------------------API----------------------------------------
@admin_required
def dashboard(request):
    members_count = Member.objects.count()
    courses_count = Course.objects.count()
    registrations_count = Registration.objects.count()
    tickets_count = Ticket.objects.filter(is_resolved=False).count()
    total_income = Registration.objects.aggregate(
        total=Sum('course__price')
    )['total'] or 0

    context = {
        'members_count': members_count,
        'courses_count': courses_count,
        'registrations': registrations_count,
        'tickets_count': tickets_count,
        'total_income': total_income,
    }
    return render(request, 'members/dashboard.html', context)
