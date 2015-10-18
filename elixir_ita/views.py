from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Course
import os.path

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATE_DIR = os.path.join(BASE_DIR, 'elixir_ita/templates/elixir_ita/')

#from django.template import RequestContext

# Create your views here.

def elixir_ita_homepage(request):
    #course = Course()
    #return render(request, 'elixir_ita/elixir_ita_homepage.html', {'course':course})
    return render(request, 'elixir_ita/elixir_ita_homepage.html')

def course_main_page(request):
    courses = Course.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'elixir_ita/course_main_page.html', {'courses':courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    COURSE_HTML = os.path.join(TEMPLATE_DIR,'course_detail_'+pk+'.html') 
    if os.path.exists(COURSE_HTML):
	return render(request, 'elixir_ita/course_detail_'+pk+'.html', {'course': course})
    else:
	return redirect('https://elearning2.uniroma1.it/course/view.php?id=3221') 
	
def application(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'elixir_ita/application_'+pk+'.html', {'course': course})

def programme(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'elixir_ita/programme_'+pk+'.html', {'course': course})

def material(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'elixir_ita/material_'+pk+'.html', {'course': course})

def unix(request):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'elixir_ita/unix.html', {'course': course})
