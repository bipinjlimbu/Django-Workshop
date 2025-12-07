from django.shortcuts import render

def index_page(request):
    return render(request, 'main/index_page.html')

def form_page(request):
    return render(request, 'main/student_form.html')