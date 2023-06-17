from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.


def news_home(request):
    new = Articles.objects.all()
    return render(request, 'news/news_home.html', {'new': new})

class NewsDatailView(DetailView):
    model=Articles
    template_name='news/detail_view.html'
    context_object_name = 'article'

class NewsUpdateView(UpdateView):
    model=Articles
    template_name='news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    model=Articles
    template_name='news/new_delete.html'
    success_url = '/new/'
    context_object_name = 'article'


def create(request):
    error = ''
    if request.method=='POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма заполнена не верно'


    form = ArticlesForm()
    data={
        'form': form,
        'error': error 
    }
    return render(request, 'news/create.html', data)
