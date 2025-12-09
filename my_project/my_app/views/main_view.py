from django.shortcuts import render, redirect, get_object_or_404
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

def update_page(request, student_id):
    get_object_or_404(student, id=student_id)
    stud = student.objects.get(id=student_id)

    if request.method == 'POST':
        stud.fullname = request.POST.get('fullname')
        stud.email = request.POST.get('email')
        stud.address = request.POST.get('address')
        stud.phone = request.POST.get('phone')
        stud.fee = request.POST.get('fee')
        stud.description = request.POST.get('description')
        stud.save()
        return redirect('index')
    
    return render(request, 'main/update_form.html', {'student': stud})

def delete_page(request, student_id):
    stud = get_object_or_404(student, id=student_id)
    stud.delete()
    return redirect('index')