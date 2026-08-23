from django.shortcuts import render


def home(request):
    students = ["Arun", "Anu", "Rahul", "Meera"]

    return render(request, "home.html", {
        "students": students
    })


def result(request, name):

    results = {
        "Arun": 85,
        "Anu": 92,
        "Rahul": 78,
        "Meera": 95
    }

    mark = results.get(name, "Result not found")

    return render(request, "result.html", {
        "name": name,
        "mark": mark
    })
