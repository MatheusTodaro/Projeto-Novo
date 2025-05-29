
from unicodedata import name
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from filmes.views import FilmeDeleteView, FilmeListView, FilmeUpdateView, NovoFilmeCreateView,FilmeDetailView
from usuario.views import usuario_view,login_view,logout_view

urlpatterns = [
    path('',FilmeListView.as_view(), name='filmes_list'),
    path ('users/', usuario_view, name= 'usuario'),
    path('admin/', admin.site.urls),
    path('filmes/',FilmeListView.as_view(), name='filmes_list'),
    path('novo_filme/', NovoFilmeCreateView.as_view(), name='novo_filme'),
    path('login/',login_view, name='login'),
    path('logout/',logout_view, name='logout'),
    path('filme/<int:pk>/',FilmeDetailView.as_view(), name='filme_detail'),
    path('filme/<int:pk>/update/', FilmeUpdateView.as_view(), name='filme_update'),
    path('filme/<int:pk>/delete/',FilmeDeleteView.as_view(),name='filme_delete')
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
