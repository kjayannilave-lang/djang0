def color_form(request):
    if request.method == 'POST':
        return render(request, 'result.html', {
            'name': request.POST.get('name'),
            'color': request.POST.get('color'),
            'form_data': request.POST
        })

    return render(request, 'index.html')
