from django.shortcuts import render
from django.shortcuts import HttpResponse
from rolepermissions.decorators import has_permission_decorator
from .models import Users

@has_permission_decorator('cadastrar_vendedor')
def cadastrar_vendedor(request):
  if request.method == "GET":
    return render(request, 'cadastrar_vendedor.html')
  if request.method == "POST":
    email = request.POST.get('email')
    senha = request.POST.get('senha')

    user = Users.objects.filter(email=email)
    if user.exists():
      return HttpResponse('E-mail ja existe')

    user = Users.objects.create_user(username=email, email=email, password=senha, cargo='V')

    return HttpResponse('Conta criada')
