from django.shortcuts import render

def username_form(request):
    return render(request, 'index.html')

def result(request):
    username = request.GET.get('username')

    return render(request, 'result.html', {
        'username': username,
        'form_data': request.GET
    })