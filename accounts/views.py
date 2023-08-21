from django.shortcuts import render
from django.contrib.auth.models import User

def doctor(request):
    return render(request, 'user/doctor_list.html', {'doctors': User.objects.all()} )
