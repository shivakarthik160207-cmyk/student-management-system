from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Student
import django.contrib.auth.decorators
from django.contrib.auth.models import User


def signup(request):

    if request.method == "POST":

        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            return render(
                request,
                "signup.html",
                {"error": "Username already exists"}
            )

        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        return redirect("/login/")

    return render(request, "signup.html")

@django.contrib.auth.decorators.login_required
def home(request):

    if request.method == "POST":
        student_id = request.POST["student_id"]
        name = request.POST["name"]
        course = request.POST["course"]

        Student.objects.create(
            user=request.user,
            student_id=student_id,
            name=name,
            course=course
        )

        messages.success(request, "Student added successfully!")

        return redirect("/home/")

    query = request.GET.get('q')

    if query:
        students = Student.objects.filter(
            user=request.user,
            name__icontains=query
        )
    else:
        students = Student.objects.filter(
            user=request.user
        )

    return render(
        request,
        "home.html",
        {"students": students}
    )

@django.contrib.auth.decorators.login_required
def edit_student(request, id):
    
    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.course = request.POST["course"]
        student.save()

        return redirect("/home/")

    return render(
        request,
        "edit_student.html",
        {"student": student}
    )


@django.contrib.auth.decorators.login_required
def delete_student(request, id):

    student = Student.objects.get(id=id)
    student.delete()

    return redirect("/home/")