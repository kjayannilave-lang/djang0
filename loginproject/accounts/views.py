from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import SignupForm


def signup(request):

    if request.method == 'POST':

        form = SignupForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            return redirect('login')

    else:
        form = SignupForm()

    return render(request, 'accounts/signup.html', {
        'form': form
    })


def user_login(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('visit_counter')

        else:

            return render(request, 'accounts/login.html', {
                'error': 'Invalid username or password'
            })

    return render(request, 'accounts/login.html')


@login_required
def visit_counter(request):

    count = request.session.get('visit_count', 0)

    count += 1

    request.session['visit_count'] = count

    return render(request, 'accounts/visit_counter.html', {
        'count': count
    })


def user_logout(request):

    logout(request)

    return redirect('login')
