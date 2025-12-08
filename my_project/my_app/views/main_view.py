from django.shortcuts import render, redirect
from my_app.models import student

def index_page(request):
    students = student.objects.all()
    return render(request, 'main/index_page.html', {'students': students})

def form_page(request):
    if request.method == 'POST':
        fullname = request.POST.get('fullname')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        fee = request.POST.get('fee')
        description = request.POST.get('description')
        
        student.objects.create(
            fullname=fullname,
            email=email,
            address=address,
            phone=phone,
            fee=fee,
            description=description
        )
        return redirect('index_page')
    
    return render(request, 'main/student_form.html')