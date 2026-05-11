from django.shortcuts import render

# Create your views here.
def login_views(request):
    return render(request, 'appUsuarios/login.html')

def registro_views(request):
    return render(request, 'appUsuarios/registro.html')