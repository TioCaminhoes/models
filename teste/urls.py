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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from biblioteca.views import (
    AuthorCreateView,
    AuthorDetailView,
    AuthorListView,
    LivroCreateView,
    LivroDeleteView,
    LivroListView,
    LivroUpdateView,
    SobreView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', LivroListView.as_view(), name='listar_livros'),
    path('authors/<int:author_id>/', AuthorDetailView.as_view(), name='author_detail'),
    path('authors/cadastrar/', AuthorCreateView.as_view(), name='cadastrar_autor'),
    path('author_list/', AuthorListView.as_view(), name='listar_autores'),
    path('livrosforms/<int:book_id>/', LivroUpdateView.as_view(), name='livro_editar'),
    path('livrosforms/novo/', LivroCreateView.as_view(), name='livro_novo'),
    path('livrosforms/<int:book_id>/excluir/', LivroDeleteView.as_view(), name='livro_excluir'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
