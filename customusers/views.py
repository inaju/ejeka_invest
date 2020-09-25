from django.views.generic import TemplateView
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, render
from .decorators import student_required

# Create your views here.

@login_required
@student_required
def take_quiz(request, pk):
    student = request.user.student 

    return render(request, 'classroom/students/take_quiz_form.html')



class SignUpView(TemplateView):
    template_name = 'registration/signup.html'
