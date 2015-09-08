from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Course

#from django.template import RequestContext

# Create your views here.

def course_main_page(request):
    courses = Course.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'elixir_ita/course_main_page.html', {'courses':courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'elixir_ita/course_detail_'+pk+'.html', {'course': course})

def application(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'elixir_ita/application.html', {'course': course})

def programme(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'elixir_ita/programme_'+pk+'.html', {'course': course})
