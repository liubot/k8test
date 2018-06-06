from django.shortcuts import render
from django.http import HttpResponse
from docker.models import hosts
import os
import socket
import hashlib

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


def add_load(request,num):
    hl = hashlib.md5()
    count = num
    count = int(count)**int(count)
    s = str(count)
    hl.update(s.encode(encoding='utf-8'))
    return HttpResponse('MD5:' + hl.hexdigest())