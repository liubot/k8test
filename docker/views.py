from django.shortcuts import render
from django.http import HttpResponse
from docker.models import hosts
import os
import socket

# Create your views here.
hostname = socket.gethostname()

def host(request):
    if hosts.objects.filter(host=hostname):
        cur_count = hosts.objects.get(host=hostname).count
        hosts.objects.filter(host=hostname).update(count=cur_count+1)
    else:
        add(hostname)
    end_count = hosts.objects.get(host=hostname).count
    return HttpResponse(hostname+':'+str(end_count))

def add(hostname):
    hosts.objects.create(host=hostname,count=1)
