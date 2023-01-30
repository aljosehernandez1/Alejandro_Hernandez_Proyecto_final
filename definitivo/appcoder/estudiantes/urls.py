from django.urls import path

from estudiantes.views import (beneficios, acerca, requisitos, planes,
saludar, #listar_estudiantes, 
listar_profesores, listar_proyectos, listar_cursos, crear_curso, buscar_curso, ver_cursos, editar_curso,
eliminar_curso, EstudiantesListView, EstudiantesUpdateView, EstudiantesDeleteView, ProfileUpdateView,
EstudiantesCreateView, EstudiantesDetailView, registro, login_v, CustomLogoutView, inicio, agregar_avatar,
)

urlpatterns = [
    path('inicio', inicio, name="inicio"),
    path('acerca', acerca, name="acerca"),
    path('requisitos', requisitos, name="requisitos"),
    path('beneficios/', beneficios, name="beneficios"),
    #path('lista-alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('planes', planes, name="planes"),
    path('lista-profesores/', listar_profesores, name="listar_profesores"),
    path('lista-proyectos/', listar_proyectos, name="listar_proyectos"),
    path('lista-cursos/', listar_cursos, name="listar_cursos"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('buscar-cursos/', buscar_curso, name="buscar_curso"),    
    path('cursos/<int:id>/', ver_cursos, name="ver_cursos"),
    path('editar-cursos/<int:id>/', editar_curso, name="editar_cursos"),
    path('eliminar-curso/<int:id>/', eliminar_curso, name="eliminar_curso"),
    #URL basadas en clases
    path('estudiantes/', EstudiantesListView.as_view(), name="listar_estudiantes"), 
    path('crear-estudiante/', EstudiantesCreateView.as_view(), name="crear_estudiantes"), 
    path('editar-estudiantes/<int:pk>/', EstudiantesUpdateView.as_view(), name="editar_estudiantes"), 
    path('eliminar-estudiante/<int:pk>/', EstudiantesDeleteView.as_view(), name="eliminar_estudiantes"), 
    path('estudiantes/<int:pk>/', EstudiantesDetailView.as_view(), name="ver_estudiantes"),
    path('editar-perfil/', ProfileUpdateView.as_view(), name="editar_perfil"),
    path('registro/', registro, name="registro"),
    path('login/', login_v, name="login"),
    path('logout/', CustomLogoutView.as_view(), name="logout"),
    path('agregar-avatar/', agregar_avatar, name="agregar_avatar"),
]
