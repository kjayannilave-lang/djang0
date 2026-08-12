from django.shortcuts import render

def color_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        color = request.POST.get('color')

        return render(request, 'result.html', {
            'name': name,
            'color': color,
            'form_data': request.POST
        })

    return render(request, 'index.html')
