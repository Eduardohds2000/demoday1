from django.shortcuts import render



# Create your views here.

def mostrar_index(request):
    return render(request, 'index.html')

def mostrar_login(request):
    return render(request, 'login.html')

def cadastro(request):
    return render (request,'form.html', {'form':form})