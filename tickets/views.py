from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def supervisorlandingpage(request):
    return render(request,'ticketlist.html')

def assignAgent(request):
    return render(request,'assignAgent.html')

def viewaddressedqueries(request):
    return render(request,'viewaddressedqueries.html')