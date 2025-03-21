from django.shortcuts import render, HttpResponse,redirect
from .models import Student1

def insert_student(request):
    student = Student1(name="manikanta", age=21, email="mani9999@gmail.com")
    student.save()
    return HttpResponse("Student record added successfully!")
def student_list(request):
    students = Student1.objects.all()
    return render(request, 'std_app/student_list.html', {'students': students})

