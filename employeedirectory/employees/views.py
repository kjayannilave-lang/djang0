from django.shortcuts import render

def home(request):
    employees = [
        {
            "name": "John",
            "job_title": "Manager",
            "salary": 50000,
            "full_time": True
        },
        {
            "name": "Alice",
            "job_title": "Designer",
            "salary": 35000,
            "full_time": False
        },
        {
            "name": "David",
            "job_title": "Developer",
            "salary": 45000,
            "full_time": True
        }
    ]

    return render(request, "employees/index.html", {"employees": employees})