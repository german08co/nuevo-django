from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


def inicio(request):
    return render(request, 'inicio/inicio.html')


@login_required
def posteos(request):
    return render(request, 'inicio/posteos.html')


def exit(request):
    logout(request)
    return redirect('inicio')
    
    

# def loguearse(request):
#     if request.method == 'POST':
#         username = request.POST['username']
#         password = request.POST['password']
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('pagina_despues_del_logueo')
#         else:
#             return render(request, 'inicio/login.html', {'error': 'Credenciales incorrectas'})
#     return render(request, 'inicio/login.html')