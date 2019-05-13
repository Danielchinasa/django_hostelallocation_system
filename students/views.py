from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from . import forms

# Create your views here.

def profile(request):
    # return HttpResponse('Hey Welcome to the HOME page')
    return render(request, 'students/profile.html')

def studentsLoginView(request):
    form = AuthenticationForm()
    return render(request, 'students/students_login.html', {'form': form})


def studentsSignupView(request):
    if request.method == 'POST':
        form = forms.CreateStudentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('/students/login')
    else:
        form = forms.CreateStudentForm()
        return render(request, 'students/students_signup.html', {'form': form})