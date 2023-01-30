from datetime import datetime
from django.db.models import Q
from django.shortcuts import render, redirect
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse
from estudiantes.forms import CursoFormulario
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from estudiantes.models import Estudiantes, Profesor, Proyecto, Curso, Planes, Avatar
from estudiantes.forms import CursoFormulario, UserRegisterForm, UserUpdateForm, AvatarFormulario
from django.contrib.auth.views import LogoutView
from django.contrib.auth  import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


def inicio(request):
        return render(
            request=request,
            template_name='estudiantes/inicio.html',
        )

def beneficios(request):
        return render(
            request=request,
            template_name='estudiantes/beneficios.html',
        )

def acerca(request):
        return render(
            request=request,
            template_name='estudiantes/acerca.html',
        )


def saludar(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )

def requisitos(request):
    return render(
        request=request,
        template_name='estudiantes/requisitos.html',
    )


#correcto
#def listar_estudiantes(request):
    contexto ={
        'estudiantes': Estudiantes.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto
    )#

@login_required
def listar_profesores(request):
    contexto ={
        'profesores': Profesor.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesores.html',
        context=contexto
    )

@login_required
def planes(request):
    contexto ={
        'planes': Planes.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/planes.html',
        context=contexto
    )

@login_required
def listar_proyectos(request):
    contexto ={
        'proyectos': Proyecto.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/lista_proyectos.html',
        context=contexto
    )
@login_required
def listar_cursos(request):
    contexto ={
        'cursos': Curso.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/lista_cursos.html',
        context=contexto
    )

@login_required
def ver_cursos(request, id):
    curso= Curso.objects.get(id=id)
    contexto ={
        'curso': curso
        
    }
    return render(
        request=request,
        template_name='estudiantes/detalle_curso.html',
        context=contexto
    )

    

@login_required
def crear_curso(request):
    if request.method =="POST":
        data = request.POST
        formulario =CursoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso(nombre=data['nombre'], comision=data['comision'], duracion=data['duracion'], descripcion=data['descripcion'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:
        formulario = CursoFormulario()
        return render(
            request=request,
            template_name='estudiantes/formulario_curso.html',
            context={'formulario': formulario},
        )
@login_required
def editar_curso(request, id):
    curso = Curso.objects.get(id=id)
    if request.method =="POST":
        formulario = CursoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            curso = Curso.objects.get(id=id)
            curso.nombre = data ['nombre']
            curso.comision = data ['comision']
            curso.duracion = data ['duracion']
            curso.descripcion = data ['descripcion']
            curso.save()
            url_exitosa = reverse('listar_cursos')
            return redirect(url_exitosa)
    else:
        inicial = {
            'nombre': curso.nombre,
            'comision': curso.comision,
            'duracion': curso.duracion,
            'descripcion': curso.descripcion,
        }
        formulario =CursoFormulario(initial=inicial)
        return render(
            request=request,
            template_name='estudiantes/formulario_curso.html',
            context={'formulario': formulario, 'curso': curso, 'es_update': True},
        )
    
@login_required
def eliminar_curso(requet, id):
    curso = Curso.objects.get(id=id)
    if requet.method =="POST":
        curso.delete()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)

@login_required   
def buscar_curso(request):
    if request.method =="POST":
        data = request.POST
        cursos = Curso.objects.filter(nombre=data['nombre'])
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )
    else:
        return render(
            request=request,
            template_name='estudiantes/busqueda_curso.html',
        )

class EstudiantesListView(LoginRequiredMixin, ListView):
    model = Estudiantes
    template_name = "estudiantes/lista_estudiantes.html"

class EstudiantesCreateView(LoginRequiredMixin, CreateView):
    model = Estudiantes
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_estudiantes')
    template_name = "estudiantes/formulario_estudiantes.html"


class EstudiantesDetailView(LoginRequiredMixin, DetailView):
    model = Estudiantes
    success_url = reverse_lazy('listar:estudiantes')
    template_name = "estudiantes/detalle_estudiantes.html"


class EstudiantesUpdateView(LoginRequiredMixin, UpdateView):
    model = Estudiantes
    fields = ['nombre', 'apellido', 'dni', 'email']
    success_url = reverse_lazy('listar_estudiantes')
    template_name = "estudiantes/formulario_estudiante.html"

class EstudiantesDeleteView(LoginRequiredMixin ,DeleteView):
    model = Estudiantes
    success_url = reverse_lazy('listar:estudiantes')
    template_name = "estudiantes/confirmar_eliminacion_estudiantes.html"


def registro(request):
    if request.method == "POST":
        formulario = UserRegisterForm(request.POST)

        if formulario.is_valid():
            formulario.save()
            url_exitosa = reverse('login')
            return redirect(url_exitosa)
    else:
        formulario = UserRegisterForm()
    return render(
        request=request,
        template_name='estudiantes/registro.html',
        context={'form': formulario},
    )

def login_v(request):
    next_url = request.GET.get('next')
    if request.method =="POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            data= form.cleaned_data
            usuario = data.get('username')
            contraseña = data.get('password')
            user = authenticate(username=usuario, password=contraseña)
            if user:
                login(request=request, user=user)
                if next_url:
                    return redirect(next_url)
                url_exitosa = reverse('listar_cursos')
                return redirect(url_exitosa)
                              
    else:
        form = AuthenticationForm()
    return render(
        request=request,
        template_name='estudiantes/login.html',
        context={'form': form},
    )

class CustomLogoutView(LogoutView):
        template_name ='estudiantes/logout.html'
        


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('inicio')
    template_name = 'estudiantes/formulario_perfil.html'

    def get_object(self, queryset=None):
        return self.request.user


@login_required 
def agregar_avatar(request):
    if request.method =="POST":
        formulario = AvatarFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            avatar = formulario.save()
            avatar.user = request.user
            avatar.save()
            url_exitosa = reverse('inicio')
            return redirect(url_exitosa)
    else:
        formulario = AvatarFormulario()
    return render(
        request=request,
        template_name='estudiantes/formulario_avatar.html',
        context={'form': formulario},
    )
