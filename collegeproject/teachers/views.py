from django.shortcuts import render


def teacher_list(request, message):
    teachers = ["John", "Priya", "David", "Anjali"]

    return render(request, "teachers/teacher_list.html", {
        "teachers": teachers,
        "message": message
    })
