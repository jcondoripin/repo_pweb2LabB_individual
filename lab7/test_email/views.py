from django.shortcuts import render
from django.core.mail import send_mail

# Create your views here.
def index(request):
    send_mail('Hola de parte de juan jose',
              'Mensaje bla bla bla',
              'juanjosecondoripinto@gmail.com',
              ['rolado5567@niback.com'],
              fail_silently=False)
    
    return render(request,'index.html')