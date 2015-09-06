from django.shortcuts import render
from django.utils import timezone
from .models import Course

#from django.template import RequestContext

# Create your views here.

def course_main_page(request):
    courses = Course.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request,'elixir_ita/course_main_page.html', {'courses':courses})
