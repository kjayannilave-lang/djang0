from django import forms
from django.shortcuts import render


class RegistrationForm(forms.Form):
    full_name = forms.CharField(
        min_length=5,
        max_length=50
    )

    email = forms.EmailField()

    password = forms.CharField(
        min_length=8,
        max_length=20,
        widget=forms.PasswordInput
    )


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)

        if form.is_valid():
            return render(request, 'success.html', {
                'name': form.cleaned_data['full_name']
            })
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {
        'form': form
    })
