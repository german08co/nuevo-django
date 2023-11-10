from django.shortcuts import render, redirect
from .models import Posteos
from .forms import formulario_posteos

def creacion_formulario(request):
    if request.method == 'POST':
        forms_posteos = formulario_posteos(request.POST)
        if forms_posteos.is_valid():
            resultado = forms_posteos.cleaned_data
            titulo_posteo = resultado.get("titulo_posteo")
            fecha_posteo = resultado.get("fecha_posteo")
            redaccion_posteo = resultado.get("redaccion_posteo")
            usuario = request.user
            posteo_nuevo = Posteos(titulo_posteo=titulo_posteo, fecha_posteo=fecha_posteo, redaccion_posteo=redaccion_posteo, usuario=usuario)
            posteo_nuevo.save()
        return redirect("inicio/inicio.html")
    else:
        return render(request, "crear_posteos.html", {"form_posteo": formulario_posteos})
