from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from members.views import Member
from django import forms

class SimpleSignupForm(UserCreationForm):
    phone = forms.CharField(max_length=15, label='شماره موبایل')
    address = forms.CharField(widget=forms.Textarea, label='ادرس', required=False)
    class Meta:
        model = User
        fields = ['username']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['username'].help_text=''
        self.fields['password1'].label = 'رمز عبور'
        self.fields['password1'].help_text=''
        self.fields['password2'].label = 'تکرار رمز عبور'
        self.fields['password2'].help_text=''

class AuthenticationForm1(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username']
    def __init__(self, request = ..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)
        self.fields['username'].label = 'نام کاربری'
        self.fields['password'].label = 'رمز عبور'




def signup_view(request):
    if request.method =='POST':
        form = SimpleSignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            Member.objects.create(
                user=user,
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address']
                )
            login(request, user)
            return redirect('members:course_list')

    else:
        form = SimpleSignupForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm1(data= request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('members:course_list')

    else:
        form = AuthenticationForm1()
    return render(request, 'accounts/login.html', {'form': form})



def logout_view(request):
    logout(request)
    return redirect('members:course_list')

