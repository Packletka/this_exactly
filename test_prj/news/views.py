from django.shortcuts import render, redirect
from .models import Articles
from .forms import ArticlesForm
from django.views.generic import DetailView, DeleteView, UpdateView, ListView


def home_news(request):
    news = Articles.objects.order_by('-date')
    print(news)
    return render(request, 'news/home_news.html', {'news': news})



def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home_news')

    form = ArticlesForm()

    data = {
        'form': form
    }
    return render(request, 'news/create.html', data)
#
#
# def delete(request):
#     return render(request, 'news/news_delete.html', {'delete': delete})


def detail_view(request):
    return render(request, 'news/detail_view.html', {'detail_view': detail_view})


class NewsDetailView(DetailView):
    model = Articles
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsDeleteView(DeleteView):
    model = Articles
    template_name = 'news/news_delete.html'
    success_url = '/news/'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm


class NewsListView(ListView):
    model = Articles
    template_name = 'news/list_view.html'
    context_object_name = 'articles'
    queryset = Articles.objects.all()






















