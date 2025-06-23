from django.shortcuts import render
from .models import Imexam

# Create your views here.

def imexam_list(request):
    exams = Imexam.objects.get_queryset()
    return render(request, 'exam/imexam_list.html', {
        'exams': exams,
    })
