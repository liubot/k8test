from django.http import HttpResponse
import socket

def index(request):
    return HttpResponse(socket.gethostname())
