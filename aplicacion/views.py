from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy

from .models import Deporte, Deportista, Entrenador, Club, Avatar
from .forms import DeporteForm, DeportistaForm, EntrenadorForm, ClubForm, \
                    RegistroUsuariosForm, UserEditForm, AvatarFormulario
from aplicacion.forms import AvatarFormulario

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth       import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def home(request):
    return render(request, "aplicacion/home.html")

@login_required
def deportes(request):
    contexto = {'deportes': Deporte.objects.all(), 'titulo': 'Listado de Actividades Deportivas' }
    return render(request, "aplicacion/deportes.html", contexto)

@login_required
def deportistas(request):
    contexto = {'deportistas': Deportista.objects.all(), 'titulo': 'Deportistas Afiliados' }
    return render(request, "aplicacion/deportistas.html", contexto)

@login_required
def entrenadores(request):
    contexto = {'entrenadores': Entrenador.objects.all(), 'titulo': 'Listado de Entrenadores' }
    return render(request, "aplicacion/entrenadores.html", contexto)

@login_required
def clubes(request):
    contexto = {'clubes': Club.objects.all(), 'titulo': 'Clubes Adheridos' }
    return render(request, "aplicacion/clubes.html", contexto)

@login_required
def deporteForm(request):
    if request.method == "POST":
        deporte = Deporte(nombre=request.POST['nombre'],
                          categoría=request.POST['categoría'])
        deporte.save()
        return HttpResponse("Se grabó con éxito el deporte!")
    return render(request, "aplicacion/deporteForm.html")

@login_required
def deportistaForm(request):
    if request.method == "POST":
        deportista = Deportista(nombre=request.POST['nombre'],
                          apellido=request.POST['apellido'],
                          email=request.POST['email'],
                          edad=request.POST['edad'])
        deportista.save()
        return HttpResponse("Se grabó con éxito el deportista!")
    return render(request, "aplicacion/deportistaForm.html")

@login_required
def entrenadorForm(request):
    if request.method == "POST":
        entrenador = Entrenador(nombre=request.POST['nombre'],
                          apellido=request.POST['apellido'],
                          email=request.POST['email'],
                          fechaAlta=request.POST['fechaAlta'])
        entrenador.save()
        return HttpResponse("Se grabó con éxito el entrenador!")
    return render(request, "aplicacion/entrenadorForm.html")

@login_required
def clubForm(request):
    if request.method == "POST":
        club = Club(nombre=request.POST['nombre'],
                    domicilio=request.POST['domicilio'])
        club.save()
        return HttpResponse("Se grabó con éxito el club!")
    return render(request, "aplicacion/clubForm.html")

@login_required
def deporteForm2(request):
    if request.method == "POST":
        miForm = DeporteForm(request.POST)
        if miForm.is_valid():
            deporte_nombre = miForm.cleaned_data.get('nombre')
            deporte_categoría =  miForm.cleaned_data.get('categoría')
            deporte = Deporte(nombre=deporte_nombre,
                             categoría=deporte_categoría)
            deporte.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = DeporteForm()    

    return render(request, "aplicacion/deporteForm2.html", {"form": miForm})

@login_required
def deportistaForm2(request):
    if request.method == "POST":
        miForm = DeportistaForm(request.POST)
        if miForm.is_valid():
            deportista_nombre = miForm.cleaned_data.get('nombre')
            deportista_apellido =  miForm.cleaned_data.get('apellido')
            deportista_email =  miForm.cleaned_data.get('email')
            deportista_edad =  miForm.cleaned_data.get('edad')
            deportista = Deportista(nombre=deportista_nombre,
                                        apellido=deportista_apellido,
                                        email=deportista_email,
                                        edad=deportista_edad)
            deportista.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = DeportistaForm()    

    return render(request, "aplicacion/deportistaForm2.html", {"form": miForm})

@login_required
def entrenadorForm2(request):
    if request.method == "POST":
        miForm = EntrenadorForm(request.POST)
        if miForm.is_valid():
            entrenador_nombre = miForm.cleaned_data.get('nombre')
            entrenador_apellido =  miForm.cleaned_data.get('apellido')
            entrenador_email =  miForm.cleaned_data.get('email')
            entrenador_fechaAlta =  miForm.cleaned_data.get('fechaAlta')
            entrenador = Entrenador(nombre=entrenador_nombre,
                                        apellido=entrenador_apellido,
                                        email=entrenador_email,
                                        fechaAlta=entrenador_fechaAlta)
            entrenador.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = EntrenadorForm()    

    return render(request, "aplicacion/entrenadorForm2.html", {"form": miForm})

@login_required
def clubForm2(request):
    if request.method == "POST":
        miForm = ClubForm(request.POST)
        if miForm.is_valid():
            club_nombre = miForm.cleaned_data.get('nombre')
            club_domicilio = miForm.cleaned_data.get('domicilio')
            club = Club(nombre=club_nombre,
                       domicilio=club_domicilio)
            club.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm = ClubForm()    

    return render(request, "aplicacion/clubForm2.html", {"form": miForm})

@login_required
def buscarDeporte(request):
    return render(request, "aplicacion/buscarDeporte.html")

@login_required
def buscar2(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        deportes = Deporte.objects.filter(nombre__icontains=patron)
        contexto = {"deportes": deportes, 'titulo': f'Deportes que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/deportes.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

@login_required
def buscarDeportista(request):
    return render(request, "aplicacion/buscarDeportista.html")

@login_required
def buscar3(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        deportistas = Deportista.objects.filter(nombre__icontains=patron)
        contexto = {"deportistas": deportistas, 'titulo': f'Deportistas que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/deportistas.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

@login_required
def buscarEntrenador(request):
    return render(request, "aplicacion/buscarEntrenador.html")

@login_required
def buscar4(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        entrenadores = Entrenador.objects.filter(nombre__icontains=patron)
        contexto = {"entrenadores": entrenadores, 'titulo': f'Entrenadores que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/entrenadores.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

@login_required
def buscarClub(request):
    return render(request, "aplicacion/buscarClub.html")

@login_required
def buscar5(request):
    if request.GET['buscar']:
        patron = request.GET['buscar']
        clubes = Club.objects.filter(nombre__icontains=patron)
        contexto = {"clubes": clubes, 'titulo': f'Clubes que tienen como patrón "{patron}"'}
        return render(request, "aplicacion/clubes.html", contexto)
    return HttpResponse("No se ingresó nada a buscar")

#____________________ Class Based View

class DeporteList(LoginRequiredMixin, ListView):
    model = Deporte

class DeporteCreate(LoginRequiredMixin, CreateView):
    model = Deporte
    fields = ['nombre', 'categoría']
    success_url = reverse_lazy('deportes')

class DeporteUpdate(LoginRequiredMixin, UpdateView):
    model = Deporte
    fields = ['nombre', 'categoría']
    success_url = reverse_lazy('deportes')

class DeporteDelete(LoginRequiredMixin, DeleteView):
    model = Deporte
    success_url = reverse_lazy('deportes')

#____________________ Deportista

class DeportistaList(LoginRequiredMixin, ListView):
    model = Deportista

class DeportistaCreate(LoginRequiredMixin, CreateView):
    model = Deportista
    fields = ['nombre', 'apellido', 'email', 'edad']
    success_url = reverse_lazy('deportistas')

class DeportistaUpdate(LoginRequiredMixin, UpdateView):
    model = Deportista
    fields = ['nombre', 'apellido', 'email', 'edad']
    success_url = reverse_lazy('deportistas')

class DeportistaDelete(LoginRequiredMixin, DeleteView):
    model = Deportista
    success_url = reverse_lazy('deportistas')

#____________________ Entrenador

class EntrenadorList(LoginRequiredMixin, ListView):
    model = Entrenador

class EntrenadorCreate(LoginRequiredMixin, CreateView):
    model = Entrenador
    fields = ['nombre', 'apellido', 'email', 'fechaAlta']
    success_url = reverse_lazy('deportistas')

class EntrenadorUpdate(LoginRequiredMixin, UpdateView):
    model = Entrenador
    fields = ['nombre', 'apellido', 'email', 'fechaAlta']
    success_url = reverse_lazy('entrenadores')

class EntrenadorDelete(LoginRequiredMixin, DeleteView):
    model = Entrenador
    success_url = reverse_lazy('entrenadores')

#____________________ Club

class ClubList(LoginRequiredMixin, ListView):
    model = Club

class ClubCreate(LoginRequiredMixin, CreateView):
    model = Club
    fields = ['nombre', 'domicilio']
    success_url = reverse_lazy('clubes')

class ClubUpdate(LoginRequiredMixin, UpdateView):
    model = Club
    fields = ['nombre', 'domicilio']
    success_url = reverse_lazy('clubes')

class ClubDelete(LoginRequiredMixin, DeleteView):
    model = Club
    success_url = reverse_lazy('clubes')

#_________________________________ Login / Logout / Registración

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            password = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)
            if user is not None:
                login(request, user)

                try:
                    avatar = Avatar.objects.get(user=request.user.id).imagen.url
                except:
                    avatar = "/media/avatares/default.png"
                finally:
                    request.session["avatar"] = avatar

                return render(request, "aplicacion/base.html", {'mensaje': f'Bienvenido a nuestro sitio {usuario}'})
            else:
                return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})
        else:
            return render(request, "aplicacion/login.html", {'form': miForm, 'mensaje': f'Los datos son inválidos'})

    miForm =   AuthenticationForm()      

    return render(request, "aplicacion/login.html", {"form":miForm})    

def register(request):
    if request.method == "POST":
        miForm = RegistroUsuariosForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            miForm.save()
            return render(request, "aplicacion/base.html")
    else:
        miForm =   RegistroUsuariosForm()      
    return render(request, "aplicacion/registro.html", {"form":miForm}) 

#______________________________Editar Perfil

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            # Actualiza la sesión del usuario para evitar cerrar la sesión después de cambiar la contraseña.
            update_session_auth_hash(request, usuario)
            return render(request, "aplicacion/base.html")
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario': usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES) # Diferente a los forms tradicionales
        if form.is_valid():
            u = User.objects.get(username=request.user)

            # ____ Para borrar el avatar viejo
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                for i in range(len(avatarViejo)):
                    avatarViejo[i].delete()

            # ____ Guardar el nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            # ___ Hago que la url de la imagen viaje en el request
            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session["avatar"] = imagen
            return render(request,"aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form })

#___________________________Acerca de

def acerca_de(request):
    return render(request, 'aplicacion/acerca_de.html')