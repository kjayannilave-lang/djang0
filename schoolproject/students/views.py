from django.shortcuts import render


def student_list(request):
    students = [
        {
            'name': 'John',
            'grade': 85,
            'passed': True
        },
        {
            'name': 'Jane',
            'grade': 72,
            'passed': True
        },
        {
            'name': 'Bob',
            'grade': 45,
            'passed': False
        },
        {
            'name': 'Alice',
            'grade': 91,
            'passed': True
        }
    ]

    return render(request, 'students.html', {
        'students': students
    })