from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def index(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        
        # Process the form data (for example, print it)
        print(f"Received form data: Name - {name}, Email - {email}")
        
        # You can perform other actions here based on the form data
        
        return HttpResponse("Form submitted successfully!")
    
    return render(request, 'index.html')

