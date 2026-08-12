from django.shortcuts import render
import re


def login_form(request):

    errors = {}
    email = ""

    if request.method == 'POST':
        email = request.POST.get('email', '')
        password = request.POST.get('password', '')

        # Email validation
        if not email:
            errors['email'] = 'Email is required.'
        elif not re.match(r'^[^@\s]+@[^@\s]+\.[^@\s]+$', email):
            errors['email'] = 'Enter a valid email address.'
        elif email.lower().endswith('@gmail.com'):
            errors['email'] = 'Gmail addresses are not allowed.'

        # Password validation
        if not password:
            errors['password'] = 'Password is required.'
        elif len(password) < 6:
            errors['password'] = 'Password must be at least 6 characters long.'

        # If everything is valid
        if not errors:
            return render(request, 'result.html', {
                'email': email
            })

    return render(request, 'login.html', {
        'errors': errors,
        'email': email
    })
