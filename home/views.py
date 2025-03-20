from django.shortcuts import render
from django.http import HttpResponse

from .models import Department,Doctors
from .forms import BookingForm

# Create your views here.
def index(request):
    # numbers= {
    #     'num1':0,
    # }
    numbers= {
        'num1':[1,2,3,4,5,6,7,8],
    }
    return render(request, 'index.html',numbers)
def about(request):
    return render(request, 'about.html')
def booking(request):
    if request.method == "POST":
        form =BookingForm(request.POST)
        if form.is_valid():
            form.save() 
            return render(request, 'confirmation.html')
    form = BookingForm()
    dict_form ={
        'form': form
    }
    return render(request, 'booking.html', dict_form)
def doctors(request):
    dict_doc = {
        'doctors': Doctors.objects.all()
    }
    return render(request, 'doctors.html', dict_doc)
def contact(request):
    return render(request, 'contact.html')
def department(request):

    dict_dep = {
        'dept': Department.objects.all()
    }
    return render(request, 'department.html', dict_dep)