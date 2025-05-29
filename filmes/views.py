from pyexpat import model
from django.shortcuts import render, redirect
from filmes.models import Filme
from filmes.forms import FilmesModelForm
from django.views.generic import ListView,CreateView,DetailView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class FilmeListView(ListView):
    model = Filme
    template_name = 'filmes.html'
    context_object_name = 'filmes'
    
    def get_queryset(self):
        filmes =  super().get_queryset().order_by('titulo')
        search = self.request.GET.get('search')
        if search:
            filmes = filmes.filter(titulo__contains=search)
        return filmes
        
class FilmeDetailView(DetailView):
    model = Filme
    template_name = 'filme_detail.html'


@method_decorator(login_required(login_url='login'), name='dispatch')
class NovoFilmeCreateView(CreateView):
    model = FilmeListView
    form_class = FilmesModelForm
    template_name = 'novo_filme.html'
    success_url = reverse_lazy('filmes_list')

@method_decorator(login_required(login_url='login'), name='dispatch')
class FilmeUpdateView(UpdateView):
    model = Filme
    form_class = FilmesModelForm
    template_name = 'filme_update.html'
    
    def get_success_url(self):
        return reverse_lazy('filme_detail', kwargs={'pk': self.object.pk})
        
@method_decorator(login_required(login_url='login'), name='dispatch')
class FilmeDeleteView(DeleteView):
    model = Filme
    template_name = 'filme_delete.html'
    success_url = reverse_lazy('filmes_list')

# class Filmesview(View): 
#     def get(self,request):
#         filmes = Filme.objects.all().order_by('titulo')
#         search = request.GET.get('search')
#         if search:
#             filmes = Filme.objects.filter(titulo__contains=search)
        
#         return render(request, 'filmes.html',{'filmes': filmes})
    
# class NovoFilmeView(View):
#     def post(self,request):
#         novo_filme_form = FilmesModelForm(request.POST,request.FILES)
#         if novo_filme_form.is_valid():
#             novo_filme_form.save()
#             return redirect('filmes_list')
#         return render(request,'novo_filme.html',{'novo_filme_form':novo_filme_form})

