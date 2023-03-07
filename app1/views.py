from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Good_evining(request):
    return HttpResponse('Hi nivas Good evining,this is your friend django')

def Had_dinner(request):
    return HttpResponse('Yes dude i have already done')