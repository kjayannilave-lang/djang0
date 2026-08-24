from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


def home(request):

    search = request.GET.get('search')

    if search:
        students = Student.objects.filter(
            name__icontains=search
        )
    else:
        students = Student.objects.all()

    return render(request, 'studentrecords/home.html', {
        'students': students,
        'search': search
    })


def add_student(request):

    if request.method == 'POST':

        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = StudentForm()

    return render(request, 'studentrecords/add_student.html', {
        'form': form
    })


def edit_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        form = StudentForm(
            request.POST,
            instance=student
        )

        if form.is_valid():
            form.save()
            return redirect('home')

    else:
        form = StudentForm(instance=student)

    return render(request, 'studentrecords/edit_student.html', {
        'form': form,
        'student': student
    })


def delete_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':

        student.delete()
        return redirect('home')

    return render(request, 'studentrecords/delete_student.html', {
        'student': student
    })
