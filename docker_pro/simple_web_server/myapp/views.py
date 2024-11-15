from django.shortcuts import render, redirect
from .forms import SimpleForm

def home_view(request):
    return redirect('simple_form') 

def simple_form_view(request):
    if request.method == 'POST':
        form = SimpleForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., print it or save it to a database)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            print(f"Name: {name}, Email: {email}")
            return render(request, 'success.html', {'name': name})
    else:
        form = SimpleForm()
    return render(request, 'form.html', {'form': form})
