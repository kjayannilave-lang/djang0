from django.shortcuts import render, redirect


def student_list(request, message):
    students = ["Arun", "Anu", "Rahul", "Meera"]

    return render(request, "students/student_list.html", {
        "students": students,
        "message": message
    })