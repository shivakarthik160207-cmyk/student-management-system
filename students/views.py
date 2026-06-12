from django.db.models.manager import BaseManager
from django.shortcuts import render, redirect
from .models import Student

def home(request):

    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(name__icontains=query)
    else:
        students: BaseManager[Student] = Student.objects.all()

    return render(
        request,
        "home.html",
        {"students": students}
    )

def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.course = request.POST["course"]
        student.save()

        return redirect("/")

    return render(
        request,
        "edit_student.html",
        {"student": student}
    )

def delete_student(request, id):

    student = Student.objects.get(id=id)
    student.delete()

    return redirect("/")