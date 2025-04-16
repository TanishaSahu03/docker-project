from django.shortcuts import render, HttpResponse
from .models import  Student
from .forms import StudentForm
from django.views.generic import CreateView


class StudentCreate(CreateView):
    model = Student
    form_class = StudentForm

    def get_success_url(self):
        return HttpResponse("HIiii")