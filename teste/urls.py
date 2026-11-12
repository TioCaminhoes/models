"""
URL configuration for teste project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from biblioteca.views import author_detail, cadastrar_autor, livro_form, listar_autores, listar_livros

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', listar_livros, name='listar_livros'),
    path('authors/<int:author_id>/', author_detail, name='author_detail'),
    path('authors/cadastrar/', cadastrar_autor, name='cadastrar_autor'),
    path('author_list/', listar_autores, name='listar_autores'),
    path('livrosforms/<int:book_id>/', livro_form, name='livro_editar'),
    path('livrosforms/novo/', livro_form, name='livro_novo'),
]
    