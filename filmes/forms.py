from django import forms
from filmes.models import Filme


class FilmesModelForm(forms.ModelForm):
    class Meta:
        model = Filme
        fields = '__all__'

    
# def clean_sinopse(self):
#     sinopse = self.cleaned_data.get('sinopse')
#     if len(sinopse) < 20:
#         self.add_error('sinopse','A sinopse deve ter pelo menos 20 caracteres.')
#     return sinopse
   
def clean_ano(self):
    ano = self.cleaned_data.get('ano')
    if ano < 1900 or ano > 2100:
        self.add_error('ano',' O ano deve estar entre 1900 e 2100.')
    return ano