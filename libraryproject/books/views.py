from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import Book
from .forms import BookForm


def home(request):
    books = Book.objects.all().order_by('id')

    paginator = Paginator(books, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'books/home.html', {
        'page_obj': page_obj
    })


def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'books/add_book.html', {
        'form': form
    })


def edit_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)

        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm(instance=book)

    return render(request, 'books/edit_book.html', {
        'form': form,
        'book': book
    })


def delete_book(request, id):
    book = get_object_or_404(Book, id=id)

    if request.method == 'POST':
        book.delete()
        return redirect('home')

    return render(request, 'books/delete_book.html', {
        'book': book
    })
