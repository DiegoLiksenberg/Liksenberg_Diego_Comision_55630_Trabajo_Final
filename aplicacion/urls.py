from django.urls import path, include
from .views import *
from django.conf.urls.static import static
from deportivo import settings

from django.contrib.auth.views import LogoutView

from . import views

urlpatterns = [
    path('', home, name="home"),
    
    

    path('deporte_form/', deporteForm, name="deporte_form"),
    path('deportista_form/', deportistaForm, name="deportista_form"),
    path('entrenador_form/', entrenadorForm, name="entrenador_form"),
    path('club_form/', clubForm, name="club_form"),
    path('deporte_form2/', deporteForm2, name="deporte_form2"),
    path('deportista_form2/', deportistaForm2, name="deportista_form2"),
    path('entrenador_form2/', entrenadorForm2, name="entrenador_form2"),
    path('club_form2/', clubForm2, name="club_form2"),

    path('buscar_deporte/', buscarDeporte, name="buscar_deporte"),
    path('buscar2/', buscar2, name="buscar2"),

    path('buscar_deportista/', buscarDeportista, name="buscar_deportista"),
    path('buscar3/', buscar3, name="buscar3"),

    path('buscar_entrenador/', buscarEntrenador, name="buscar_entrenador"),
    path('buscar4/', buscar4, name="buscar4"),

    path('buscar_club/', buscarClub, name="buscar_club"),
    path('buscar5/', buscar5, name="buscar5"),

    path('deportes/', DeporteList.as_view(), name="deportes" ),
    path('create_deporte/', DeporteCreate.as_view(), name="create_deporte" ),    
    path('update_deporte/<int:pk>/', DeporteUpdate.as_view(), name="update_deporte" ),
    path('delete_deporte/<int:pk>/', DeporteDelete.as_view(), name="delete_deporte" ),

    path('deportistas/', DeportistaList.as_view(), name="deportistas" ),
    path('create_deportista/', DeportistaCreate.as_view(), name="create_deportista" ),    
    path('update_deportista/<int:pk>/', DeportistaUpdate.as_view(), name="update_deportista" ),
    path('delete_deportista/<int:pk>/', DeportistaDelete.as_view(), name="delete_deportista" ),

    path('entrenadores/', EntrenadorList.as_view(), name="entrenadores" ),
    path('create_entrenador/', EntrenadorCreate.as_view(), name="create_entrenador" ),    
    path('update_entrenador/<int:pk>/', EntrenadorUpdate.as_view(), name="update_entrenador" ),
    path('delete_entrenador/<int:pk>/', EntrenadorDelete.as_view(), name="delete_entrenador" ),

    path('clubes/', ClubList.as_view(), name="clubes" ),
    path('create_club/', ClubCreate.as_view(), name="create_club" ),    
    path('update_club/<int:pk>/', ClubUpdate.as_view(), name="update_club" ),
    path('delete_club/<int:pk>/', ClubDelete.as_view(), name="delete_club" ),

    path('login/', login_request, name="login" ),   
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout" ),
    path('registro/', register, name="registro" ),

    path('editar_perfil/', editarPerfil, name='editar_perfil'),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar" ),

    path('acerca_de/', views.acerca_de, name='acerca_de'),

]
