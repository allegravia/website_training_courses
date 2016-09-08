from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from .models import Course, Trainer
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
    courses = Course.objects.filter(published_date__lte=timezone.now()).order_by('course_date')
    #courses = Course.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #if you want the courses published in reverse order, use the following line (and comment the previous one)
    #courses = Course.objects.filter(published_date__lte=timezone.now()).order_by('published_date').reverse()
    return render(request,'elixir_ita/course_main_page.html', {'courses':courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    COURSE_HTML = os.path.join(TEMPLATE_DIR,'course_detail_'+pk+'.html') 
    if os.path.exists(COURSE_HTML):
	return render(request, 'elixir_ita/course_detail_'+pk+'.html', {'course': course})
    else:
        if pk == '3': #NGSBeMM2015
	    return redirect('https://elearning2.uniroma1.it/course/view.php?id=3221') 
        elif pk == '6':  #RNASeq2016
	    return redirect('http://rnaseqworkshop2016.evosexdevo.eu/') 
	elif pk == '7': #HPCMolDyn2016
            return redirect('http://www.hpc.cineca.it/content/high-performance-molecular-dynamics') 
	elif pk == '8': #HPCMolDyn2016-PRACE
            return redirect('https://events.prace-ri.eu/event/416/')
        elif pk == '12': #NETTAB2016:
            return redirect('http://www.igst.it/nettab/2016/')
        elif pk == '13': #NETTAB2016:
            return redirect('http://www.igst.it/nettab/2016/programme/tutorials/')

	
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

def events(request):
    return render(request, "elixir_ita/events.html") 

def trainers_main_page(request):
    return render(request, "elixir_ita/trainers_main_page.html") 

def contacts(request):
    return render(request, "elixir_ita/contacts.html") 

def excelerate_ttt(request):
    return render(request, "elixir_ita/excelerate_ttt.html") 

def ttt_at_bits2016(request):
    return render(request, "elixir_ita/ttt_at_bits2016.html") 

def course_programme_2016(request):
    return render(request, "elixir_ita/course_programme_2016.html") 

def trainer(request, trainer_name, cn):
    trainer = get_object_or_404(Trainer, pk=trainer_name)
    course = get_object_or_404(Course, pk=cn)
    #return render(request, 'elixir_ita/trainers/'+trainer_name+'/'+trainer_name+'.html', {'trainer': trainer})
    return render(request, 'elixir_ita/trainers/trainer_info.html', {'trainer': trainer, 'course': course})


